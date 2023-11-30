from threading import Event
from threading import Thread
import launch
import launch_pytest
import launch_ros
import pytest
import rclpy
from rclpy.node import Node
from interfaces.srv import Arm


@launch_pytest.fixture
def generate_test_description():
    return launch.LaunchDescription(
        [
            launch_ros.actions.Node(package="arm_node", executable="arm_node"),
        ]
    )


@pytest.mark.launch(fixture=generate_test_description)
def test_check_if_msgs_published():
    rclpy.init()
    try:
        node = MakeTestNode("test_node")
        node.start_client()
        assert node.send_request, "finish"
    finally:
        rclpy.shutdown()


class MakeTestNode(Node):
    def __init__(self, name="test_node"):
        super().__init__(name)
        self.msg_event_object = Event()

    def start_client(self):
        self.cli = self.create_client(Arm, "arm_node")
        self.ros_spin_thread = Thread(
            target=lambda node: rclpy.spin(node), args=(self,)
        )
        self.ros_spin_thread.start()

    def send_request(self):
        self.req = Arm.Request()
        self.req.length = 0.1
        self.res = self.cli.call_async(self.req)
        return self.res.finish
