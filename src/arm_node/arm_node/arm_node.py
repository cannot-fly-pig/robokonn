import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from interfaces.srv import Arm

try:
    import RPI.GPIO as GPIO
except ImportError:
    import Mock.GPIO as GPIO


import time
import math

PI = math.pi


class MotorController:
    def __init__(self, forward_ping, back_ping):
        self.forward_ping = forward_ping
        self.back_ping = back_ping

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(forward_ping, GPIO.OUT)
        GPIO.setup(back_ping, GPIO.OUT)

    def move_motor(self, w, ms):
        t = ms / 1000
        step_deg = 1.8

        if w > 0:
            ping = self.forward_ping
        elif w < 0:
            ping = self.back_ping
            w *= -1

        step = math.floor(w * t / step_deg)
        hz = step / t
        print(hz)

        self.pi = GPIO.PWM(ping, hz)
        self.pi.start(50)

    def stop_motor(self):
        self.pi.stop()


class ArmNode(Node):
    def __init__(self):
        super().__init__("arm_node")
        self.motor = MotorController(26, 27)
        self.srv = self.create_service(Arm, "arm_node", self.server_callback)

    def server_callback(self, req, res):
        length = req.length
        r = 1
        w = length / (r * 2 * PI)
        self.motor.move_motor(w, 1000)
        time.sleep(1)
        self.motor.stop_motor()
        res.finish = "finish"

        return res


def main():
    rclpy.init()
    node = ArmNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    executor.spin()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
