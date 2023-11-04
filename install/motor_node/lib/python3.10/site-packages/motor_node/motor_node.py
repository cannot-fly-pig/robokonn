import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from std_msgs.msg import String
import numpy as np
from interfaces.srv import GoingCameraData
from interfaces.srv import BackingCameraData
from interfaces.srv import DistanceSensorData
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
        self.gap = -10
        self.degree = -10
        self.distance = -10
        self.task = 'standby'
        self.max_gap = 10

        self.pub = self.create_publisher(String, 'motor_node', 10)
        self.sub = self.create_subscription(String, 'main_node', self.mainCallback, 10, callback_group=self.client_cb_group)
        self.timer_period = 1
        self.timer = self.create_timer(self.timer_period, self.timerCallback, callback_group=self.timer_cb_group)
        self.going_camera_client = self.create_client(GoingCameraData, 'going_camera_data')
        self.backing_camera_client = self.create_client(BackingCameraData, 'backing_camera_data')
        self.distance_sensor_client = self.create_client(DistanceSensorData, 'distance_sensor_data')

        while not self.going_camera_client.wait_for_service(timeout_sec=1):
            self.get_logger().info('waiting for going camera client...')

        while not self.distance_sensor_client.wait_for_service(timeout_sec=1):
            self.get_logger().info('waiting for sensor client...')

        self.goging_request = GoingCameraData.Request()
        self.backing_request = BackingCameraData.Request()
        self.distance_request = DistanceSensorData.Request()

    def mainCallback(self, msg):
        self.task = msg.data

    def timerCallback(self):
        if self.task == 'go':
            result = self.sendRequest(client=self.going_camera_client, request=self.goging_request)
            print('gap is: ')
            print(result.gap)
            self.gap = result.gap
            #self.goToGoal()
            self.finishTask()
        if self.task == 'putBaggage':
            self.finishTask()
        if self.task == 'turn':
            self.halfTurn()
            self.finishTask()
        if self.task == 'back':
            result = self.sendRequest(client=self.backing_camera_client, request=self.backing_request)
            print('pos is: ')
            print(result.pos)
            print('degree is: ')
            print(result.degree)
            print('gap is: ')
            print(result.gap)
            self.pos = result.pos
            self.degree = result.degree
            self.gap = result.gap
            result = self.sendRequest(client=self.distance_sensor_client, request=self.distance_request)
            print('distance is: ')
            print(result.distance)
            self.distance = result.distance
            #self.backFromGoal()
            self.finishTask()
        if self.task == 'takeBaggage':
            self.finishTask()

    def sendRequest(self, client, request):
        self.future = client.call_async(request)
        while not self.future.done():
            None
        return self.future.result()

    def finishTask(self):
        msg = String()
        msg.data = 'fin'
        self.pub.publish(msg)

    def halfTurn(self):
        #self.moveMotor(self.culcInvertKinematics(0, 0, PI/4), 4000)
        None

    def goToGoal(self):
        run_time = 300
        while math.abs(self.gap) > self.max_gap:
            #self.moveMotor(self.culcInvertKinematics(min(self.gap, 0.3), 0, 0), run_time)
            None
        
        while self.distance > self.max_distance:
            #self.moveMotor(self.culcInvertKinematics(0, min(self.distance, 0.3), 0), run_time)
            None

    def culcInvertKinematics(self, vx, vy, wz):
        #[frontleft, frontright, rearleft, rearright]
        r = 0.05
        lx = 0.13
        ly = 0.12
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
