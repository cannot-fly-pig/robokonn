import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusive_callbackGroup

try:
    import pigpio
except ImportError:
    None

from interfaces.srv import Distance


class SensorNode(Node):
    def __init__(self):
        super().__init__("sensor_node")
        self.service_cb_group = MutuallyExclusive_callbackGroup()
        self.timer_cb_group = MutuallyExclusive_callbackGroup()

        self.distance = -10
        self.timer = self.create_timer(
            0.04, self.timer_callback, callback_group=self.timer_cb_group
        )
        self.pub = self.create_publisher(Distance, "direction_node", 10)
        try:
            self.pi = pigpio.pi()
        except ModuleNotFoundError:
            self.pi = None

    def timer_callback(self):
        sensor_addresses = [0x40, 0x50, 0x60, 0x70]
        distance = []
        for address in sensor_addresses:
            distance.append(self.read_distance(address))

        self.distance = min(distance)
        msg = Distance()
        msg.top_left = self.distance[0]
        msg.top_right = self.distance[1]
        msg.bottom_left = self.distance[2]
        msg.bottom_right = self.distance[3]
        self.pub.publish(msg)

    def read_distance(self, sensor_address):
        register = 0x81
        byte = 2
        sensor = self.pi.i2c_open(1, sensor_address)
        _b, d = self.pi.i2c_read_i2c_block_data(sensor, register, byte)
        distance = ((d[0] * 16 + d[1]) / 16) / 4 / 100

        return distance


def main():
    rclpy.init()
    node = SensorNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    executor.spin()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
