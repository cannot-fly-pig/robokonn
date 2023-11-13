import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import RPi.GPIO as GPIO  


class MainNode(Node):
    def __init__(self):
        super().__init__('main_node')
        self.pub = self.create_publisher(String, 'main_node', 10)
        self.sub = self.create_subscription(String, 'motor_node', self.subCallback, 10)
        button_pin = 12
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(
            button_pin,
            GPIO.FALLING,
            callback=self.button_callback,
            bouncetime=200
        )

        self.taskIndex = 0
        self.taskList = ['takeBaggage', 'turn', 'go', 'putBaggage', 'turn', 'back']
        self.task = 'standby'
        self.timer = self.create_timer(1, self.sendTask)

    def sendTask(self):
        if self.task != 'standby':
            msg = String()
            msg.data = self.task
            self.pub.publish(msg)
            print(self.task)

    def subCallback(self, msg):
        self.taskIndex += 1
        if self.taskIndex >= len(self.taskList):
            self.taskIndex = 0
        self.task = self.taskList[self.taskIndex]

    def button_callback(self, channel):
        self.task = self.taskList[self.taskIndex]


def main():
    rclpy.init()
    node = MainNode()
    rclpy.spin(node)
    node.sendTask()


if __name__ == '__main__':
    main()
