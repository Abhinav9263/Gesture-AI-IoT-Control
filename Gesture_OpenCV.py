import cv2
import mediapipe as mp
import requests

ESP32_IP = "http://192.168.31.89"  # Replace with your ESP32 IP

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
last_state = None

def count_fingers(hand_landmarks):
    count = 0
    tips = [8, 12, 16, 20]
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1
    return count

while True:
    success, frame = cap.read()
    if not success:
        print("❌ Failed to grab frame")
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers = count_fingers(hand_landmarks)

            if fingers == 4 and last_state != "ON":
                print("🖐️ Gesture: OPEN → Sending ON")
                requests.get(f"{ESP32_IP}/on")
                last_state = "ON"
            elif fingers == 0 and last_state != "OFF":
                print("✊ Gesture: FIST → Sending OFF")
                requests.get(f"{ESP32_IP}/off")
                last_state = "OFF"

    cv2.imshow("Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
