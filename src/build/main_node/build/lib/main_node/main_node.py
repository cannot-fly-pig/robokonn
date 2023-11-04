import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MainNode(Node):
    def __init__(self):
        super().__init__('main_node')
        self.pub = self.create_publisher(String, 'main_node', 10)
        self.sub = self.create_subscription(String, 'motor_node', self.subCallback, 10)
        self.taskIndex = 0
        self.taskList = ['takeBaggage', 'turn', 'go', 'putBaggage', 'turn', 'back']
        self.task = self.taskList[self.taskIndex]
        self.timer = self.create_timer(1, self.sendTask)

    def sendTask(self):
        msg = String()
        msg.data = self.task
        self.pub.publish(msg)
        print(self.task)
    
    def subCallback(self, msg):
        self.taskIndex += 1
        if self.taskIndex >= len(self.taskIndex):
            self.taskIndex = 0


def main():
    rclpy.init()
    node = MainNode()
    rclpy.spin(node)
    node.sendTask()


if __name__ == '__main__':
    main()