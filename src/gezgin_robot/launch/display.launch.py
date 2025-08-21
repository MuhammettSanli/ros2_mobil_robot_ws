import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
import xacro
import launch 

def generate_launch_description():

    # Bu argüman, GUI'yi kullanıp kullanmayacağımızı belirler
    use_joint_state_publisher_gui = DeclareLaunchArgument(
        name='gui',
        default_value='True',
        description='Flag to enable joint_state_publisher_gui'
    )

    # URDF dosyamızın tam yolunu bul
    pkg_path = os.path.join(get_package_share_directory('gezgin_robot'))
    urdf_file_path = os.path.join(pkg_path, 'urdf', 'gezgin.urdf')

    # URDF dosyasını oku
    robot_description_config = xacro.process_file(urdf_file_path)
    robot_description = {'robot_description': robot_description_config.toxml()}

    # robot_state_publisher düğümünü yapılandır
    # Bu düğüm, URDF'yi okur ve robotun durumunu /tf topic'inde yayınlar
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description]
    )

    # joint_state_publisher_gui düğümünü yapılandır
    # Bu düğüm, eklemleri hareket ettirmek için bir arayüz sağlar
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        condition=launch.conditions.IfCondition(LaunchConfiguration('gui'))
    )

    # RViz2 düğümünü yapılandır
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
    )

    return LaunchDescription([
        use_joint_state_publisher_gui,
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])

