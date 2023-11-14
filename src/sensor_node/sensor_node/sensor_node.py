import rclpy
from rclpy.node import Node

try:
    import pigpio
except ImportError:
    None

from interfaces.msg import Distance


class SensorNode(Node):
    def __init__(self):
        super().__init__("sensor_node")

        self.timer = self.create_timer(0.04, self.timer_callback)
        self.pub = self.create_publisher(Distance, "sensor_node", 10)
        try:
            self.pi = pigpio.pi()
        except NameError:
            self.pi = None

    def timer_callback(self):
        sensor_addresses = [0x40, 0x50, 0x60, 0x70]
        distance = []
        for address in sensor_addresses:
            distance.append(self.read_distance(address))

        msg = Distance()
        msg.top_left = distance[0]
        msg.top_right = distance[1]
        msg.bottom_left = distance[2]
        msg.bottom_right = distance[3]
        self.pub.publish(msg)

    def read_distance(self, sensor_address):
        register = 0x81
        byte = 2

        try:
            sensor = self.pi.i2c_open(1, sensor_address)
            _b, d = self.pi.i2c_read_i2c_block_data(sensor, register, byte)
            distance = ((d[0] * 16 + d[1]) / 16) / 4 / 100
        except AttributeError:
            distance = 10.0

        if distance > 50:
            distance = 9999.0

        return distance


def main():
    rclpy.init()
    node = SensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
