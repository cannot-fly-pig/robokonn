import rclpy
from rclpy.node import Node
from interfaces.msg import Finish, Task


class MainNode(Node):
    def __init__(self):
        super().__init__("main_node")
        self.pub = self.create_publisher(Task, "main_node", 10)
        self.sub = self.create_subscription(
            Finish, "motor_node", self.sub_callback, 10
        )

        self.task_index = 0
        self.task_list = [
            "takeBaggage",
            "turn",
            "go",
            "putBaggage",
            "turn",
            "back",
        ]
        self.task = self.task_list[self.task_index]
        self.timer = self.create_timer(0.1, self.send_task)

    def send_task(self):
        if self.task != "standby":
            msg = Task()
            msg.task = self.task
            self.pub.publish(msg)
            print(self.task)

    def sub_callback(self, msg):
        self.task_index += 1
        if self.task_index >= len(self.task_list):
            self.task_index = 0

        self.task = self.task_list[self.task_index]


def main():
    rclpy.init()
    node = MainNode()
    rclpy.spin(node)
    node.send_task()


if __name__ == "__main__":
    main()
