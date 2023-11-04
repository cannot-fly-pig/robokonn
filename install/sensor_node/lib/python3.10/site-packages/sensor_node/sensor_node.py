import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
import random
import smbus
import time
from interfaces.srv import DistanceSensorData

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.service_cb_group = MutuallyExclusiveCallbackGroup()
        self.timer_cb_group = MutuallyExclusiveCallbackGroup()

        self.distance = -10
        self.distance_sensor_service = self.create_service(DistanceSensorData, 'distance_sensor_data', self.distanceSensorCallback, callback_group=self.service_cb_group)
        self.timer = self.create_timer = self.create_timer(0.3, self.readSensorValue, callback_group=self.timer_cb_group)
        #self.bus=smbus.SMBus(1)
        self.address_gpy2=0x40
        self.register_gpyu=0x5E
        self.register_gpys=0x5F

    def distanceSensorCallback(self, request, response):
        if self.distance < 10:
            self.readSensorValue() 
        
        response.distance = self.distance
        print('service called!')

        return response
        

    def readSensorValue(self):
        self.distance = random.randint(1, 5)
    #    data=0
    #    for i in range(10):
    #        #11-4bit data
    #        ue = self.bus.read_word_data(self.address_gpy2, self.register_gpyu)
    #        #3-0bit data
    #        shita = self.bus.read_word_data(self.address_gpy2, self.register_gpys)
    #        ue = ue & 0xff
    #        shita = shita & 0xff
    #        kobetu = ((ue*16+shita)/16)/4
    #        data +=kobetu
    #        time.sleep(0.005)

    #    average=data/10
    #    self.distance = average


def main():
    rclpy.init()
    node = SensorNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    executor.spin()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()