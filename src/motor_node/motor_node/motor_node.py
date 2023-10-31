import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from std_msgs.msg import String
import numpy as np
from interfaces.srv import GoingCameraData
#import RPi.GPIO as GPIO
import time
import math


class MotorNode(Node):
    def __init__(self):
        super().__init__('motor_node')
        self.client_cb_group = MutuallyExclusiveCallbackGroup()
        self.timer_cb_group = MutuallyExclusiveCallbackGroup()

        self.gap = None
        self.task = 'standby'
        self.max_gap = 10

        self.sub = self.create_subscription(String, 'main_node', self.mainCallback, 10, callback_group=self.client_cb_group)
        self.timer_period = 1
        self.timer = self.create_timer(self.timer_period, self.timerCallback, callback_group=self.timer_cb_group)
        self.going_camera_client = self.create_client(GoingCameraData, 'going_camera_data')

        while not self.going_camera_client.wait_for_service(timeout_sec=1):
            self.get_logger().info('waiting for going camera client...')

        self.goging_request = GoingCameraData.Request()

    def mainCallback(self, msg):
        self.task = msg.data

    def timerCallback(self):
        if self.task == 'go':
            result = self.sendRequest(client=self.going_camera_client, request=self.goging_request)
            print(result.gap)
            self.gap = result.gap
            #self.goToGoal(self)

    def sendRequest(self, client, request):
        self.future = client.call_async(request)
        while not self.future.done():
            None
        return self.future.result()


    def goToGoal(self):
        run_time = 300
        while self.gap > self.max_gap:
            wList = self.culcInvertKinematics(self.gap/(run_time /1000), 0, 0)
            for i, w in enumerate(wList):
                #TODO 非同期にしたほうが良さそう？
                self.moveMotor(w, run_time, i)

    def culcInvertKinematics(self, vx, vy, wz):
    #[frontleft, frontright, rearleft, rearright]
        r = 50
        lx = 10
        ly = 10
        mat = (1/r)* np.matrix([[1, -1, -(lx+ly)],
                                [1, 1, (lx+ly)],
                                [1, 1, -(lx+ly)],
                                [1, -1, (lx+ly)]])

        w = np.dot(mat, np.array([vx, vy, wz]))
        w  = w * 180 / 3.14

        return w[0]

    def moveMotor(self, w, t, n):
        step_deg = 1.8

        if w > 0 :
            ping = n
        else:
            ping = n+1
            w *= -1

        step = math.floor(w * t / step_deg)
        interval = t / (step - 1) - 4

        for i in step:
            self.sendPulse(ping)
            time.sleep(interval / 1000)

    def sendPulse(self, n):
        GPIO.output(n, 1)
        time.sleep(2 / 1000)
        GPIO.output(n, 0)
        time.sleep(2 / 1000)
        

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
