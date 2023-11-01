import rclpy
from rclpy.node import Node
import random
from interfaces.srv import GoingCameraData

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.going_camera_service = self.create_service(GoingCameraData, 'going_camera_data', self.goingCameraCallback)

    def goingCameraCallback(self, request, response):
        response.gap = random.randint(1, 100)
        print('service called!')
        return response

def main(): 
    rclpy.init()
    node = CameraNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()