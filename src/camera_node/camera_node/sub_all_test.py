import rclpy
from rclpy.node import Node

from team6_msgs.msg import Goal, Back, Direction      


class Subscriber_all(Node):

    def __init__(self):
        super().__init__('goal_subscriber')
        self.subscription_goal = self.create_subscription(
            Goal,                                
            'goal_pub',
            self.callback_goal,
            10)
        self.subscription_goal

        self.subscription_back = self.create_subscription(
            Back,                                
            'back_pub',
            self.callback_back,
            10)
        self.subscription_back

        self.subscription_dir = self.create_subscription(
                Direction,                                   
                'direction_pub',
                self.callback_dir,
                10)
        self.subscription_dir


    def callback_goal(self, msg):
            self.get_logger().info('GoalSub diff : "%d"' % msg.diff) 

    def callback_back(self, msg):
            self.get_logger().info('BackSub pos, degree, diff : "%s %s %s"' % (msg.pos, msg.degree, msg.diff)) 

    def callback_dir(self, msg):
            self.get_logger().info('DirSub direction : "%s"' % msg.direction)


def main(args=None):
    rclpy.init(args=args)

    subscriber_all = Subscriber_all()

    rclpy.spin(subscriber_all)

    subscriber_all.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()