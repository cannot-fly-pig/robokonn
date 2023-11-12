import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MainNodeTest(Node):

    def __init__(self):
        super().__init__('main_node_test')
        self.pub = self.create_publisher(String, 'main_node', 10)

        self.pub_count = 0
        self.taskIndex = 0
        self.taskList = ['takeBaggage', 'turn', 'go', 'putBaggage', 'turn', 'back']
        #self.task = 'standby'
        self.timer = self.create_timer(1, self.sendTask)


    def sendTask(self):
        msg = String()
        if self.pub_count == 10:
            self.taskIndex += 1
            if self.taskIndex >= len(self.taskList):
                self.taskIndex = 0
            self.pub_count = 0
        msg.data = self.taskList[self.taskIndex]
        self.pub.publish(msg)
        print(self.taskList[self.taskIndex])
        self.pub_count += 1
            


def main(args=None):
    rclpy.init(args=args)

    main_node_test = MainNodeTest()

    rclpy.spin(main_node_test)

    main_node_test.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
