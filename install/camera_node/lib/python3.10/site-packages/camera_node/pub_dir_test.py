import rclpy
from rclpy.node import Node

from team6_msgs.msg import Direction


class DirectionPublisher(Node):

    def __init__(self):
        super().__init__('direction_publisher')
        self.publisher_ = self.create_publisher(Direction, 'direction_pub', 10)
        timer_period = 3  # seconds
        self.timer = self.create_timer(timer_period, self.callback)
        self.i = 0

    def callback(self):
        msg = Direction()
        msg.direction = 'goal'
        self.publisher_.publish(msg)
        self.get_logger().info('direction : "%s %s"' % (msg.direction, self.i))
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    direction_publisher = DirectionPublisher()

    rclpy.spin(direction_publisher)

    direction_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
