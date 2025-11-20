import cv2
import pyttsx3
import mediapipe as mp

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speaking speed

def speak(text):
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def start_object_detection():
    net = cv2.dnn.readNetFromCaffe(
        'MobileNetSSD_deploy.prototxt',
        'MobileNetSSD_deploy.caffemodel'
    )

    classes = [
        "background", "aeroplane", "bicycle", "bird", "boat",
        "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
        "dog", "horse", "motorbike", "person", "pottedplant",
        "sheep", "sofa", "train", "tvmonitor"
    ]

    cap = cv2.VideoCapture(0)
    speak("Object detection started")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
        net.setInput(blob)
        detections = net.forward()

        detected_objects = set()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.5:
                idx = int(detections[0, 0, i, 1])
                label = classes[idx]
                detected_objects.add(label)

                box = detections[0, 0, i, 3:7] * [w, h, w, h]
                (startX, startY, endX, endY) = box.astype("int")
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        if detected_objects:
            spoken_text = ", ".join(detected_objects)
            speak(f"I see: {spoken_text}")

        cv2.imshow("Object Detection", frame)

        if cv2.waitKey(1) == 27:  # ESC key to break
            break

    cap.release()
    cv2.destroyAllWindows()
    speak("Object detection ended")






def start_hand_gesture_detection():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    speak("Hand gesture detection started")

    while True:
        success, img = cap.read()
        if not success:
            break

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Simple finger counter based on y-coordinate of landmarks
                finger_tips = [8, 12, 16, 20]
                fingers_up = 0

                for tip_id in finger_tips:
                    if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y:
                        fingers_up += 1

                cv2.putText(img, f"Fingers: {fingers_up}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 2)
                speak(f"I see {fingers_up} fingers up")

        cv2.imshow("Hand Gesture Detection", img)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    speak("Hand gesture detection ended")
