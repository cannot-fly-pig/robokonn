import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from std_msgs.msg import String
import numpy as np
from interfaces.srv import GoingCameraData
from interfaces.srv import BackingCameraData
from interfaces.srv import DistanceSensorData
from interfaces.msg import Goal, Back, Direction
#import RPi.GPIO as GPIO
import time
import math

PI = math.pi

class MotorNode(Node):
    def __init__(self):
        super().__init__('motor_node')
        self.client_cb_group = MutuallyExclusiveCallbackGroup()
        self.timer_cb_group = MutuallyExclusiveCallbackGroup()

        self.pos = ''
        self.diff = -10
        self.degree = -10
        self.distance = -10
        self.task = 'standby'
        self.max_diff = 10

        self.subscription_goal = self.create_subscription(
            Goal,                                
            'goal_pub',
            self.goalCallback,
            10)
        self.subscription_goal

        self.subscription_back = self.create_subscription(
            Back,                                
            'back_pub',
            self.backCallback,
            10)
        self.subscription_back

        self.subscription_distance = self.create_subscription(
            Direction,                                   
            'direction_pub',
            self.distanceCallback,
            10)
        self.subscription_distance

        self.timer_period = 1
        self.timer = self.create_timer(self.timer_period, self.timerCallback, callback_group=self.timer_cb_group)

    def goalCallback(self, msg):
        self.diff = msg.diff
        
    def backCallback(self, msg):
        self.diff = msg.diff
        self.pos = msg.pos
        self.degree = msg.degree

    def distanceCallback(self, msg):
        self.distance = msg.distance

    def timerCallback(self):
        if self.task == 'go':
            self.goToGoal()
            self.finishTask()
        if self.task == 'putBaggage':
            self.finishTask()
        if self.task == 'turn':
            self.halfTurn()
            self.finishTask()
        if self.task == 'back':
            self.backFromGoal()
            self.finishTask()
        if self.task == 'takeBaggage':
            self.finishTask()

    def finishTask(self):
        msg = String()
        msg.data = 'fin'
        self.pub.publish(msg)

    def halfTurn(self):
        w = self.culcInvertKinematics(0, 0, PI/2)
        self.moveMotor(w, 2)

    def goToGoal(self):
        run_time = 300

        while math.abs(self.distance) > self.max_distance:
            w = self.culcInvertKinematics(max(self.distance, 0.1), 0, 0)
            self.moveMotor(w, run_time)

        while math.abs(self.diff) > self.max_diff:
            if self.diff > 0:
                w = self.culcInvertKinematics(0, min(-1*self.diff, -0.1), 0)
            else:
                w = self.culcInvertKinematics(0, max(self.diff, 0.1), 0)

            self.moveMotor(w, run_time)

    def backFromGoal(self):
        run_time = 300

        while self.pos != 'center':
            w = self.culcInvertKinematics(0, 0.3, 0)
            self.moveMotor(w, run_time)

        while self.distance > 0.2:
            w = self.culcInvertKinematics(0.2, 0, 0)
            self.moveMotor(w, run_time)

            deg = self.degree / 180 * PI * (-1)
            if abs(deg) > PI / 15:
                w = self.culcInvertKinematics(0, 0, deg)
                self.moveMotor(w, 1)


    def culcInvertKinematics(self, vx, vy, wz):
        #[frontleft, frontright, rearleft, rearright]
        r = 0.05
        lx = 0.092
        ly = 0.14
        mat = (1/r)* np.matrix([[1, -1, -(lx+ly)],
                        [1, 1, (lx+ly)],
                        [1, 1, -(lx+ly)],
                        [1, -1, (lx+ly)]])

        w = np.dot(mat, np.array([vx, vy, wz]))
        w  = w * 180 / 3.14

        return w.tolist()[0]

    def moveMotor(self, wList, ms):
        t = ms / 1000
        step_deg = 1.8
        ping_offset = 18
        GPIOList = []

        for i in range(4):
            w = wList[i]

        if w > 0 :
            ping = ping_offset + i * 2
        else:
            ping = ping_offset + i * 2 + 1
            w *= -1

        step = math.floor(w * t / step_deg)
        hz = step / t
        print(hz)
        GPIOList.append(GPIO.PWM(ping, hz))

        for pi in GPIOList:
            print(pi)
            pi.start(50)

        time.sleep(t)

        for pi in GPIOList:
            pi.stop()

        GPIO.setmode ( GPIO.BCM )
        for i in range(18, 26):
            GPIO.setup (i, GPIO.OUT)

def main():
    rclpy.init()
    node = MotorNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    executor.spin()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
