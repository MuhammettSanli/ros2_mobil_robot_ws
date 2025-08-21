🤖 ROS 2 & Gazebo Mobil Robot Simülasyon Projesi 


📖 Projeye Genel Bakış

Bu depo, ROS 2 Jazzy ve Gazebo Harmonic kullanarak sıfırdan geliştirilen otonom bir mobil robot simülasyon projesinin tüm aşamalarını içermektedir. Proje, robot modellemesinden başlayarak, fiziksel simülasyon, sensör entegrasyonu ve otonom navigasyon (SLAM) yeteneklerine kadar geniş bir yelpazeyi kapsamayı hedeflemektedir.

🗺️ Proje Yol Haritası

Proje, Git dalları (branch) kullanılarak aşamalar halinde geliştirilmektedir. Her bir dal, projenin belirli bir fonksiyonel kilometre taşını temsil eder.


✅ main Dalı - Robot Modelleme ve Görselleştirme

Durum: Tamamlandı.

Robotun URDF (xacro) formatında 3D modeli oluşturuldu.

Model, robot_state_publisher ve joint_state_publisher kullanılarak RViz üzerinde başarılı bir şekilde görselleştirildi.

Bu dal, projenin en son stabil ve test edilmiş versiyonunu içerir.


⏳ feature/gazebo-control Dalı - Gazebo Simülasyonu ve Kontrol

Durum: Geliştirme Aşamasında.

Hedef: Robot modelini Gazebo Harmonic simülasyon ortamında çalıştırmak ve ros2_control kullanarak hareket ettirmek.



📅 feature/slam-mapping Dalı - Sensör Entegrasyonu ve Haritalama

Durum: Planlanıyor.

Hedef: Robota bir Lidar sensörü eklemek, slam_toolbox ile haritalama yapmak ve otonom navigasyon temellerini atmak.



🚀 Başlarken
Bu projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin.

### Ön Gereksinimler
İşletim Sistemi: Ubuntu 24.04

ROS 2 Sürümü: Jazzy Jalisco

Simülatör: Gazebo Harmonic

Gerekli Paketler: ros-dev-tools, ros-jazzy-ros-gz
