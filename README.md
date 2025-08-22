# 🤖 ROS 2 & Gazebo Mobil Robot Simülasyon Projesi - Gazebo Kontrol Dalı

# <img width="1854" height="1132" alt="image" src="https://github.com/user-attachments/assets/bc74fda7-ba3e-4a4d-92b0-cbb355682ce7" />


---

## 📖 Bu Dal Hakkında (`feature/gazebo-control`)

Bu dal, projenin **Gazebo Harmonic** simülasyon ortamında çalışan versiyonunu içermektedir. Robot, Gazebo'nun yerel fizik eklentileri (`gz-sim-diff-drive-system`) ile kontrol edilmektedir ve tüm hareketleri anlık olarak RViz üzerinde de görselleştirilmektedir.

**Bu dalda tamamlananlar:**
-   Robot modeli Gazebo'ya başarıyla aktarıldı.
-   `gz-sim-diff-drive-system` eklentisi ile diferansiyel sürüş kontrolü sağlandı.
-   `ros_gz_bridge` ile Gazebo ve ROS 2 arasında tam çift yönlü iletişim kuruldu (`/cmd_vel`, `/odom`, `/tf`, `/joint_states`).
-   Robot, klavyeden (`teleop_twist_keyboard`) veya herhangi bir `/cmd_vel` yayıncısından gelen komutlarla hareket ettirilebilir.
-   Gazebo ve RViz'i senkronize bir şekilde başlatan tek bir `launch` dosyası (`gazebo.launch.py`) oluşturuldu.

---

## 🚀 Simülasyonu Çalıştırma

### ### Ön Gereksinimler
-   **İşletim Sistemi:** Ubuntu 24.04
-   **ROS 2 Sürümü:** Jazzy Jalisco
-   **Simülatör:** Gazebo Harmonic
-   **Gerekli Paketler:** `ros-dev-tools`, `ros-gz-bridge`, `ros-gz-sim`, `teleop-twist-keyboard`

### ### Kurulum ve Çalıştırma

1.  **Depoyu Klonlayın ve Bu Dala Geçin:**
    ```bash
    git clone [https://github.com/SENIN_KULLANICI_ADIN/REPO_ADIN.git](https://github.com/SENIN_KULLANICI_ADIN/REPO_ADIN.git)
    cd REPO_ADIN
    git checkout feature/gazebo-control
    ```

2.  **Projeyi Derleyin:**
    ```bash
    # Çalışma alanının ana dizinine gidin (örn: ~/ros2_ws)
    colcon build --packages-select my_robot_description
    ```

3.  **Ortamı Tanıtın (Source Edin):**
    ```bash
    source install/setup.bash
    ```

4.  **Simülasyonu Başlatın:**
    ```bash
    ros2 launch my_robot_description gazebo.launch.py
    ```

5.  **(Yeni Bir Terminalde) Robotu Kontrol Edin:**
    ```bash
    # Yeni bir terminal açın ve source edin
    source install/setup.bash
    ros2 run teleop_twist_keyboard teleop_twist_keyboard
    ```
