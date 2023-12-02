import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup
import numpy as np
from interfaces.msg import Goal, Back, Task, Finish, Distance
from interfaces.srv import Arm

try:
    import RPi.GPIO as GPIO
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


class MotorNode(Node):
    def __init__(self):
        super().__init__("motor_node")
        self.client_cb_group = MutuallyExclusiveCallbackGroup()
        self.timer_cb_group = MutuallyExclusiveCallbackGroup()

        self.pos = ""
        self.diff = -10
        self.degree = -10
        self.distance = {
            "top_left": -9999,
            "top_right": -9999,
            "bottom_left": -9999,
            "bottom_right": -9999,
            "average": -9999,
        }
        self.task = "standby"
        self.max_diff = 0.05
        self.motor = [
            MotorController(21, 20),
            MotorController(18, 19),
            MotorController(25, 24),
            MotorController(23, 22),
        ]

        self.pub = self.create_publisher(Finish, "motor_node", 10)

        self.main_sub = self.create_subscription(
            Task, "main_node", self.main_callback, 10
        )
        self.distance_sub = self.create_subscription(
            Distance, "sensor_node", self.distance_callback, 10
        )
        self.goal_sub = self.create_subscription(
            Goal, "goal_pub", self.goal_callback, 10
        )
        self.back_sub = self.create_subscription(
            Back, "back_pub", self.back_callback, 10
        )
        self.timer_period = 1
        self.timer = self.create_timer(
            self.timer_period,
            self.timer_callback,
            callback_group=self.timer_cb_group,
        )
        self.cli = self.create_client(
            Arm, "arm_node", callback_group=self.client_cb_group
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
        self.distance["top_left"] = msg.top_left
        self.distance["top_right"] = msg.top_right
        self.distance["bottom_left"] = msg.bottom_left
        self.distance["bottom_right"] = msg.bottom_right
        self.distance["average"] = np.average(
            list(
                filter(
                    lambda x: x != 9999,
                    [
                        msg.top_left,
                        msg.top_right,
                        msg.bottom_left,
                        msg.bottom_right,
                    ],
                )
            )
        )
        print(self.distance["average"])

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
            self.take_baggage()
            self.finish_task()

    def finish_task(self):
        msg = Finish()
        msg.finish = "fin"
        self.pub.publish(msg)

    def half_turn(self):
        w = self.culc_invert_kinematics(0, 0, PI)
        self.move_to(w, 2000)

    def go_to_goal(self):
        run_time = 300

        while math.abs(self.diff) > self.max_diff:
            if self.diff > 0:
                w = self.culc_invert_kinematics(
                    0, min(-1 * self.diff, -0.1), 0
                )
            else:
                w = self.culc_invert_kinematics(0, max(self.diff, 0.1), 0)

            self.move_to(w, run_time)

        while self.distance["average"] > 0.2:
            w = self.culc_invert_kinematics(
                max(self.distance["average"], 0.1), 0, 0
            )
            self.move_to(w, run_time)

    def back_from_goal(self):
        run_time = 300

        while self.pos != "center":
            w = self.culc_invert_kinematics(0, 0.3, 0)
            self.move_to(w, run_time)

        while self.distance["average"] > 0.2:
            w = self.culc_invert_kinematics(0.2, 0, 0)
            self.move_to(w, run_time)

            deg = self.degree / 180 * PI * (-1)
            if abs(deg) > PI / 15:
                w = self.culc_invert_kinematics(0, 0, deg)
                self.move_to(w, 1000)

        deg = self.degree / 180 * PI * (-1)
        w = self.culc_invert_kinematics(0, 0, deg)
        self.move_to(w, 1000)

    def take_baggage(self):
        while self.distance["average"] == -9999:
            None

        run_time = 300

        while self.distance["bottom_left"] > 0.05:
            w = self.culc_invert_kinematics(0.05, 0, 0)
            self.move_to(w, run_time)

    def put_baggage(self):
        self.req = Arm.Request()
        self.req.length = 0.16
        self.cli.call_async(self.req)

        w = self.culc_invert_kinematics(0.1, 0, 0)
        self.move_to(w, 1800)

        self.req = Arm.Request()
        self.req.length = 0.025
        self.cli.call_async(self.req)

        w = self.culc_invert_kinematics(-0.1, 0, 0)
        self.move_to(w, 1800)

        self.req = Arm.Request()
        self.req.length = -0.185
        self.cli.call_async(self.req)

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

    def move_to(self, w_list, ms):
        t = ms / 1000

        for i in range(4):
            self.motor[i].move_motor(w_list[i], ms)

        time.sleep(t)

        for i in range(4):
            self.motor[i].stop_motor()


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
