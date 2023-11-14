from threading import Event
from threading import Thread
import launch
import launch_pytest
import launch_ros
import pytest
import rclpy
from rclpy.node import Node
from interfaces.msg import Finish, Task
import time


@launch_pytest.fixture
def generate_test_description():
    return launch.LaunchDescription(
        [
            launch_ros.actions.Node(
                package="main_node", executable="main_node"
            ),
        ]
    )


@pytest.mark.launch(fixture=generate_test_description)
def test_check_if_msgs_published():
    rclpy.init()
    try:
        node = MakeTestNode("test_node")
        node.start_subscriber()
        msgs_received_flag = node.msg_event_object.wait(timeout=5.0)
        assert msgs_received_flag, "Did not receive msgs !"
        print(node.task)
        assert node.task == "takeBaggage"
    finally:
        rclpy.shutdown()


@pytest.mark.launch(fixture=generate_test_description)
def test_check_if_msgs_has_changed_when_task_finished():
    rclpy.init()
    try:
        node = MakeTestNode("test_node")
        node.start_subscriber()
        node.start_publisher()
        task_list = ["takeBaggage", "turn", "go", "putBaggage", "turn", "back"]
        for i in task_list:
            msgs_received_flag = node.msg_event_object.wait(timeout=5.0)
            assert msgs_received_flag, "Did not receive msgs !"
            assert node.task == i
            node.publish_fin()
            time.sleep(0.5)

    finally:
        rclpy.shutdown()


class MakeTestNode(Node):
    def __init__(self, name="test_node"):
        super().__init__(name)
        self.msg_event_object = Event()
        self.task = ""

    def start_subscriber(self):
        self.subscription = self.create_subscription(
            Task, "main_node", self.subscriber_callback, 10
        )

        self.ros_spin_thread = Thread(
            target=lambda node: rclpy.spin(node), args=(self,)
        )
        self.ros_spin_thread.start()

    def start_publisher(self):
        self.pub = self.create_publisher(Finish, "motor_node", 10)

    def publish_fin(self):
        msg = Finish()
        msg.finish = "finish"
        self.pub.publish(msg)

    def subscriber_callback(self, msg):
        self.msg_event_object.set()
        self.task = msg.task
        print(self.task)
