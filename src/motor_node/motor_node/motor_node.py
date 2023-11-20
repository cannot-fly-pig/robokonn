import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusive_callbackGroup
from std_msgs.msg import String
import numpy as np
from interfaces.msg import Goal, Back, Task, Finish, Distance

try:
    import RPI.GPIO as GPIO
except ImportError:
    import Mock.GPIO as GPIO


import time
import math

PI = math.pi


class MotorNode(Node):
    def __init__(self):
        super().__init__("motor_node")
        self.client_cb_group = MutuallyExclusive_callbackGroup()
        self.timer_cb_group = MutuallyExclusive_callbackGroup()

        self.pos = ""
        self.diff = -10
        self.degree = -10
        self.distance = -10
        self.task = "standby"
        self.max_diff = 10

        self.pub = self.create_publisher(Finish, "motor_node", 10)

        self.main_sub = self.create_subscription(
            Task, "main_node", self.main_callback
        )
        self.distance_sub = self.create_subscription(
            Distance, "sensor_node", self.distance_callback
        )
        self.goal_sub = self.create_subscription(
            Goal, "goal_pub", self.goal_callback
        )
        self.back_sub = self.create_subscription(
            Back, "back_pub", self.back_callback
        )
        self.timer_period = 1
        self.timer = self.create_timer(
            self.timer_period,
            self.timer_callback,
            callback_group=self.timer_cb_group,
        )

    def main_callback(self, msg):
        self.task = msg.task

    def goal_callback(self, msg):
        self.diff = msg.diff

    def back_callback(self, msg):
        self.diff = msg.diff
        self.pos = msg.pos
        self.degree = msg.degree

    def distance_callback(self, msg):
        self.top_left = msg.top_left
        self.top_right = msg.top_right
        self.bottom_left = msg.bottom_left
        self.bottom_right = msg.bottom_right

    def timer_callback(self):
        if self.task == "go":
            self.go_to_goal()
            self.finish_task()
        if self.task == "putBaggage":
            self.finish_task()
        if self.task == "turn":
            self.half_turn()
            self.finish_task()
        if self.task == "back":
            self.back_from_goal()
            self.finish_task()
        if self.task == "takeBaggage":
            self.finish_task()

    def finish_task(self):
        msg = String()
        msg.finish = "fin"
        self.pub.publish(msg)

    def half_turn(self):
        w = self.culc_invert_kinematics(0, 0, PI / 2)
        self.move_motor(w, 2)

    def go_to_goal(self):
        run_time = 300

        while math.abs(self.distance) > self.max_distance:
            w = self.culc_invert_kinematics(max(self.distance, 0.1), 0, 0)
            self.move_motor(w, run_time)

        while math.abs(self.diff) > self.max_diff:
            if self.diff > 0:
                w = self.culc_invert_kinematics(
                    0, min(-1 * self.diff, -0.1), 0
                )
            else:
                w = self.culc_invert_kinematics(0, max(self.diff, 0.1), 0)

            self.move_motor(w, run_time)

    def back_from_goal(self):
        run_time = 300

        while self.pos != "center":
            w = self.culc_invert_kinematics(0, 0.3, 0)
            self.move_motor(w, run_time)

        while self.distance > 0.2:
            w = self.culc_invert_kinematics(0.2, 0, 0)
            self.move_motor(w, run_time)

            deg = self.degree / 180 * PI * (-1)
            if abs(deg) > PI / 15:
                w = self.culc_invert_kinematics(0, 0, deg)
                self.move_motor(w, 1)

    def culc_invert_kinematics(self, vx, vy, wz):
        # [frontleft, frontright, rearleft, rearright]
        r = 0.05
        lx = 0.092
        ly = 0.14
        mat = (1 / r) * np.matrix(
            [
                [1, -1, -(lx + ly)],
                [1, 1, (lx + ly)],
                [1, 1, -(lx + ly)],
                [1, -1, (lx + ly)],
            ]
        )

        w = np.dot(mat, np.array([vx, vy, wz]))
        w = w * 180 / 3.14

        return w.tolist()[0]

    def move_motor(self, w_list, ms):
        t = ms / 1000
        step_deg = 1.8
        ping_offset = 18
        gpio_list = []

        for i in range(4):
            w = w_list[i]

        if w > 0:
            ping = ping_offset + i * 2
        else:
            ping = ping_offset + i * 2 + 1
            w *= -1

        step = math.floor(w * t / step_deg)
        hz = step / t
        print(hz)
        gpio_list.append(GPIO.PWM(ping, hz))

        for pi in gpio_list:
            print(pi)
            pi.start(50)

        time.sleep(t)

        for pi in gpio_list:
            pi.stop()

        GPIO.setmode(GPIO.BCM)
        for i in range(18, 26):
            GPIO.setup(i, GPIO.OUT)


def main():
    rclpy.init()
    node = MotorNode()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    executor.spin()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
