import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MainNode(Node):
    def __init__(self):
        super().__init__('main_node')
        self.pub = self.create_publisher(String, 'main_node', 10)
        self.setTask('go')
        self.timer = self.create_timer(1, self.sendTask)

    def setTask(self, task):
        msg = String()
        msg.data = task
        self.task = msg
    
    def sendTask(self):
        self.pub.publish(self.task)
        print(self.task)


def main():
    rclpy.init()
    node = MainNode()
    rclpy.spin(node)
    node.sendTask()


if __name__ == '__main__':
    main()