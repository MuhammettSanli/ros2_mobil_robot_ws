import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro  # XACRO kütüphanesini içeri aktarıyoruz


def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    # URDF dosyasının yolunu bul
    urdf_file_name = 'my_robot.urdf.xacro'
    urdf_path = os.path.join(
        get_package_share_directory('my_robot_description'),
        'urdf',
        urdf_file_name)
    
    # XACRO dosyasını işle ve URDF'ye çevir
    doc = xacro.process_file(urdf_path)
    robot_desc = doc.toxml()

    # robot_state_publisher düğümünü oluştur
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}]
    )

    # joint_state_publisher_gui düğümünü oluştur
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui'
    )

    # RViz düğümünü oluştur
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])