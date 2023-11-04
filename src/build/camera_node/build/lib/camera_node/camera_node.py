import rclpy
from rclpy.node import Node
import random
import math
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
from std_msgs.msg import String
from interfaces.srv import GoingCameraData, BackingCameraData

PI = math.pi

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.client_cb_group = MutuallyExclusiveCallbackGroup()
        self.service_cb_group = MutuallyExclusiveCallbackGroup()
        self.timer_cb_group = MutuallyExclusiveCallbackGroup()

        self.task = 'standby'
        self.gap = -10
        self.pos = ''
        self.degree = PI

        self.sub = self.create_subscription(String, 'main_node', self.mainCallback, 10, callback_group=self.client_cb_group)
        self.going_camera_service = self.create_service(GoingCameraData, 'going_camera_data', self.goingCameraCallback, callback_group=self.service_cb_group)
        self.backing_camera_service = self.create_service(BackingCameraData, 'backing_camera_data', self.backingCameraCallback, callback_group=self.service_cb_group)
        self.timer = self.create_timer(0.3, self.readCameraValue, callback_group=self.timer_cb_group)

    def mainCallback(self, msg):
        self.task = msg.data

    def goingCameraCallback(self, request, response):
        response.gap = self.gap
        print('service called!')
        return response

    def backingCameraCallback(self, request, response):
        response.pos = self.pos
        response.degree = self.degree
        response.gap = self.gap
        print('service called!')
        return response

    def readCameraValue(self):
        if self.task == 'go':
            self.gap = random.randint(1, 5)

        if self.task == 'back':
            self.pos = 'center'
            self.degree = PI / random.randint(1, 5)
            self.gap = random.randint(1, 5)

def main():
    rclpy.init()
    node = CameraNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    executor.spin()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()