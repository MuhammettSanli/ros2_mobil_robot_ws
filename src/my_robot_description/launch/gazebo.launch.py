import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():

    # Paket yollarını bul
    pkg_path = get_package_share_directory('my_robot_description')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    # XACRO'yu işle ve robot tanımını al
    xacro_file = os.path.join(pkg_path, 'urdf', 'my_robot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)
    robot_desc = robot_description_config.toxml()

    # RViz konfigürasyon dosyasının yolunu al
    rviz_config_file = os.path.join(pkg_path, 'rviz', 'gazebo_config.rviz')

    # Gazebo simülasyonunu başlat
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')]),
        launch_arguments={'gz_args': f'-r {pkg_path}/worlds/my_world.world'}.items()
    )

    # Robotu Gazebo'da oluştur (spawn)
    spawn_entity_node = Node(package='ros_gz_sim', executable='create',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_robot',
                                   '-z', '0.1'], # <-- YENİ EKLENEN SATIR BU
                        output='screen')

    # robot_state_publisher düğümü (RViz için gerekli)
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc, 'use_sim_time': True}]
    )

    # Gazebo ve ROS 2 arasında köprü kur (SENİN BULDUĞUN DOĞRU VERSİYON)
    gz_ros_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
            '/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model'
        ],
        parameters=[{'use_sim_time': True}],
        output='screen'
    )

    # RViz'i başlat
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_file],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_entity_node,
        robot_state_publisher_node,
        gz_ros_bridge,
        rviz_node
    ])