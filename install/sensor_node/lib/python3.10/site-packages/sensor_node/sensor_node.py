import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
#import pigpio
from interfaces.srv import Distance

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.service_cb_group = MutuallyExclusiveCallbackGroup()
        self.timer_cb_group = MutuallyExclusiveCallbackGroup()

        self.distance = -10
        self.timer = self.create_timer(0.04, self.timerCallback, callback_group=self.timer_cb_group)
        self.pub = self.create_publisher(Distance, 'direction_node', 10)
        #self.bus=smbus.SMBus(1)
        self.address_gpy2=0x40
        self.register_gpyu=0x5E
        self.register_gpys=0x5F

    def timerCallback(self):
        pi = pigpio.pi()
        sensor_addresses = [0x40, 0x50, 0x60, 0x70]  
        distance = []
        for address in sensor_addresses:
            distance.append(self.readDistance(pi, address))

        self.distance = min(distance)
        msg = Distance()
        msg.distance = self.distance
        self.pub.publish(msg)


    def readDistance(self, pi, sensor_address):
        REGISTER = 0x81
        BYTE = 2 
        sensor = pi.i2c_open(1, sensor_address) 
        b, d = pi.i2c_read_i2c_block_data(sensor, REGISTER, BYTE)
        ans = ((d[0]*16+d[1]) / 16) / 4 / 100
        self.distance = ans


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