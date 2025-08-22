# 🤖 ROS 2 & Gazebo Mobil Robot Simülasyon Projesi

Bu depo, **ROS 2 Jazzy** ve **Gazebo Harmonic** kullanarak sıfırdan geliştirilen bir mobil robot simülasyon projesinin tüm aşamalarını içermektedir. Proje, robot modellemesinden başlayarak, fiziksel simülasyon, sensör entegrasyonu ve otonom navigasyon (SLAM) yeteneklerine kadar geniş bir yelpazeyi kapsamayı hedeflemektedir.

---

## 🗺️ Proje Geliştirme Dalları (Branches)

Proje, Git dalları (branch) kullanılarak aşamalar halinde geliştirilmektedir. Her bir dal, projenin belirli bir fonksiyonel kilometre taşını temsil eder.

### ✅ `main` Dalı - Robot Modelleme ve RViz Görselleştirme
-   **Durum:** Stabil ve Tamamlandı.
-   **Açıklama:** Bu dal, projenin en temel ve stabil halini içerir. Robotun 3D modeli (URDF/XACRO) ve bu modeli **sadece RViz üzerinde** (simülasyon olmadan) görselleştirmek için gerekli olan `display.launch.py` dosyasını barındırır.

<img width="1866" height="1167" alt="sonprojev1" src="https://github.com/user-attachments/assets/6c883808-cbc5-49de-a004-10294a049b9e" />
<img width="1866" height="1167" alt="sonprojeüstv1" src="https://github.com/user-attachments/assets/043e9272-904a-482b-ad52-a5a6e8dfec44" />

### ✅ `feature/gazebo-control` Dalı - Gazebo Simülasyonu ve Kontrol
-   **Durum:** Stabil ve Tamamlandı.
-   **Açıklama:** Projenin tam fonksiyonlu simülasyon versiyonunu içerir. Robot, Gazebo'da **yerel fizik eklentileri** (`gz-sim-diff-drive-system`) ile hareket ettirilebilir ve RViz ile senkronize bir şekilde çalışır.
-   > _**Projenin güncel geliştirme ve testleri bu dalda yapılmaktadır.**_

   
<img width="1854" height="1132" alt="GazeboRvizEntegre" src="https://github.com/user-attachments/assets/3b4b377a-e039-4555-bbee-1a1477266785" />
     

### 📅 `feature/slam-mapping` Dalı - Haritalama (Gelecek Aşama)
-   **Durum:** Planlanıyor.
-   **Açıklama:** Robota bir Lidar sensörü eklenerek `slam_toolbox` ile haritalama yapılması hedeflenmektedir.

---

## 🚀 Bu Dalı (`main`) Çalıştırma

Bu dal, robot modelini fizik simülasyonu olmadan, sadece RViz'de görüntülemek içindir.

### Ön Gereksinimler
-   **İşletim Sistemi:** Ubuntu 24.04
-   **ROS 2 Sürümü:** Jazzy Jalisco
-   **Gerekli Paketler:** `ros-dev-tools`, `ros-jazzy-urdf-launch`

### Kurulum ve Çalıştırma

1.  **Depoyu Klonlayın:**
    ```bash
    # Yeni bir çalışma alanı oluşturun ve içine girin
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src

    # Depoyu klonlayın
    git clone [https://github.com/MuhammettSanli/ros2_mobil_robot_ws.git](https://github.com/MuhammettSanli/ros2_mobil_robot_ws.git)
    ```

2.  **Projeyi Derleyin:**
    ```bash
    cd ~/ros2_ws
    colcon build --packages-select my_robot_description
    ```

3.  **Ortamı Tanıtın (Source Edin):**
    ```bash
    source install/setup.bash
    ```

4.  **RViz'de Modeli Görüntüleyin:**
    ```bash
    ros2 launch my_robot_description display.launch.py
    ```
