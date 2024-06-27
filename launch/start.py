import os 
from ament_index_python.packages import get_package_share_directory
import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import SetLaunchConfiguration
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import ComposableNodeContainer
from launch_ros.actions import LoadComposableNodes
from launch_ros.descriptions import ComposableNode
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node

from launch import LaunchContext

import yaml


def generate_launch_description():
    launch_arguments = []

    context = LaunchContext()
    camera_param_path_fl = os.path.join(
        FindPackageShare("lucid_vision_driver").perform(context),
        "param/param.fl.yaml"
    )

    camera_param_path_fr = os.path.join(
        FindPackageShare("lucid_vision_driver").perform(context),
        "param/param.fr.yaml"
    )

    camera_param_path_fm = os.path.join(
        FindPackageShare("lucid_vision_driver").perform(context),
        "param/param.fm.yaml"
    )

    camera_param_path_rl = os.path.join(
        FindPackageShare("lucid_vision_driver").perform(context),
        "param/param.rl.yaml"
    )

    camera_param_path_rr = os.path.join(
        FindPackageShare("lucid_vision_driver").perform(context),
        "param/param.rr.yaml"
    )

    camera_param_path_rm = os.path.join(
        FindPackageShare("lucid_vision_driver").perform(context),
        "param/param.rm.yaml"
    )

    camera_front_left = Node(
        package="lucid_vision_driver",
        executable="arena_camera_node_exe",
        name="arena_camera_node_front_left",
        namespace="camera_lucid",
        parameters=[camera_param_path_fl],
        remappings=[
        ],
    )
    camera_front_right = Node(
        package="lucid_vision_driver",
        executable="arena_camera_node_exe",
        name="arena_camera_node_front_right",
        namespace="camera_lucid",
        parameters=[camera_param_path_fr],
        remappings=[
        ],
    )

    camera_front_middle = Node(
        package="lucid_vision_driver",
        executable="arena_camera_node_exe",
        name="arena_camera_node_front_middle",
        namespace="camera_lucid",
        parameters=[camera_param_path_fm],
        remappings=[
        ],
    )

    camera_rear_left = Node(
        package="lucid_vision_driver",
        executable="arena_camera_node_exe",
        name="arena_camera_node_rear_left",
        namespace="camera_lucid",
        parameters=[camera_param_path_rl],
        remappings=[
        ],
    )

    camera_rear_right = Node(
        package="lucid_vision_driver",
        executable="arena_camera_node_exe",
        name="arena_camera_node_rear_right",
        namespace="camera_lucid",
        parameters=[camera_param_path_rr],
        remappings=[
        ],
    )

    camera_rear_middle = Node(
        package="lucid_vision_driver",
        executable="arena_camera_node_exe",
        name="arena_camera_node_rear_middle",
        namespace="camera_lucid",
        parameters=[camera_param_path_rm],
        remappings=[
        ],
    )

    return LaunchDescription(
        [
            *launch_arguments,
            camera_front_left,
            camera_front_right,
            camera_front_middle,
            camera_rear_left,
            camera_rear_right,
            camera_rear_middle,
        ]
    )