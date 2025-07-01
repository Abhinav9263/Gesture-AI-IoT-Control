# 🤖 Gesture-Controlled Smart Appliances (ESP32 + Python + MediaPipe)

Control your home appliances like an LED (as bulb) and 3.7V motor (as fan) using real-time hand gestures via a webcam and ESP32 over Wi-Fi.

---

## 📸 Features

- 🖐️ Open Palm → Turn ON LED (Bulb)
- ✌️ Two Fingers → Turn ON Fan
- ✊ Fist → Turn OFF both LED and Fan
- Real-time hand tracking using **MediaPipe**
- Wireless communication with **ESP32 WebServer**
- Easily expandable for smart home use cases

---

## 🔧 Technologies Used

| Platform | Tools |
|----------|-------|
| AI       | MediaPipe, OpenCV (Python) |
| IoT      | ESP32 WebServer (Arduino) |
| Language | Python, C++ (Arduino)     |

---

## 🗂️ Project Structure

gesture-controlled-smart-appliances/
│
├── esp32_code/
│ └── gesture_appliance.ino # ESP32 web server code
│
├── python_code/
│ └── gesture_controller.py # Hand tracking + control via PC webcam
│
├── hardware_diagram/
│ └── circuit_diagram.png # ESP32 + motor + LED wiring diagram
│
├── README.md
└── requirements.txt

---

## 🖥️ Python Setup (PC Side)

### 📦 Requirements
Install required packages:

```bash
pip install opencv-python mediapipe requests
▶️ Run the Gesture Controller
Update your ESP32 IP in the script and run:


python gesture_controller.py
🔌 ESP32 Setup
Upload gesture_appliance.ino to ESP32

Set your Wi-Fi credentials in the sketch

Use these routes to control:

/ledon → Turn ON LED

/ledoff → Turn OFF LED

/fanon → Turn ON Fan

/fanoff → Turn OFF Fan

🔋 Hardware Used
ESP32 DevKit v1

LED (Bulb simulation)

3.7V DC Motor (Fan simulation)

2N2222 NPN Transistor

1N4007 Diode

220Ω Resistor

USB Power or Battery

🔌 Wiring Diagram
✅ Safe switching via transistor
✅ Diode for flyback protection
✅ Common GND for ESP32 and motor supply


📽️ Demo
🔜 Coming soon: Demo video of live gesture-based control


            Made with ❤️ by Abhinav


🪄 License
This project is licensed under the MIT License.


