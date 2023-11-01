import rclpy
from rclpy.node import Node
import random
from interfaces.srv import DistanceSensorData

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.distance_sensor_service = self.create_service(DistanceSensorData, 'distance_sensor_data', self.distanceSensorCallback)

    def distanceSensorCallback(self, request, response):
        response.distance = random.randint(1, 100)
        print('service called!')
        return response

def main(): 
    rclpy.init()
    node = SensorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()