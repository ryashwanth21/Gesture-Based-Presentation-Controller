import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Track last detection time for responsiveness control
last_detected_time = time.time()

# Minimum time interval between actions
def is_time_elapsed(interval=0.5):
    global last_detected_time
    current_time = time.time()
    if current_time - last_detected_time > interval:
        last_detected_time = current_time
        return True
    return False

# Detect gesture function
def detect_gesture(hand_landmarks, hand_type):
    fingers = [False] * 5  # Track which fingers are up

    # Thumb
    fingers[0] = hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x if hand_type == "Right" else \
        hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x
    # Index Finger
    fingers[1] = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
    # Middle Finger
    fingers[2] = hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y

    # Swipe Left (Left Hand)
    if hand_type == "Left" and fingers[1] and \
            hand_landmarks.landmark[8].x < hand_landmarks.landmark[5].x - 0.15 and is_time_elapsed(0.8):
        return "LEFT_SWIPE"

    # Swipe Right (Right Hand)
    if hand_type == "Right" and fingers[1] and \
            hand_landmarks.landmark[8].x > hand_landmarks.landmark[5].x + 0.15 and is_time_elapsed(0.8):
        return "RIGHT_SWIPE"

    # Next Slide (Right Hand, Index Finger Up)
    if hand_type == "Right" and fingers[1] and not any(fingers[2:]) and is_time_elapsed(0.8):
        return "NEXT"

    # Previous Slide (Left Hand, Index Finger Up)
    if hand_type == "Left" and fingers[1] and not any(fingers[2:]) and is_time_elapsed(0.8):
        return "PREVIOUS"

    # Start/Stop Presentation (Thumbs Up, Right Hand)
    if fingers[0] and is_time_elapsed(0.8):
        return "START_STOP"

    # Zoom In (Two Fingers Up, Right Hand)
    if fingers[1] and fingers[2] and is_time_elapsed(0.8):
        return "ZOOM_IN"

    # Zoom Out (Two Fingers Up, Left Hand)
    if hand_type == "Left" and fingers[1] and fingers[2] and is_time_elapsed(0.8):
        return "ZOOM_OUT"

    return "NONE"

# Start the camera feed
def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip and process the frame
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks, hand_label in zip(results.multi_hand_landmarks, results.multi_handedness):
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Detect hand type (Right/Left)
                hand_type = hand_label.classification[0].label

                # Detect gesture
                gesture = detect_gesture(hand_landmarks, hand_type)
                print("Gesture Detected:", gesture)

                # Perform actions based on the gesture
                if gesture == "LEFT_SWIPE":
                    pyautogui.press('left')
                elif gesture == "RIGHT_SWIPE":
                    pyautogui.press('right')
                elif gesture == "NEXT":
                    pyautogui.press('right')
                elif gesture == "PREVIOUS":
                    pyautogui.press('left')
                elif gesture == "START_STOP":
                    pyautogui.press('f5')
                elif gesture == "ZOOM_IN":
                    pyautogui.keyDown('ctrl')
                    pyautogui.scroll(500)  # Adjust for zoom in
                    pyautogui.keyUp('ctrl')
                elif gesture == "ZOOM_OUT":
                    pyautogui.keyDown('ctrl')
                    pyautogui.scroll(-500)  # Adjust for zoom out
                    pyautogui.keyUp('ctrl')

        # Resize camera feed window and display
        frame_height, frame_width, _ = frame.shape
        resized_frame = cv2.resize(frame, (300, 200))  # Resize the camera feed
        cv2.imshow('Camera Feed (for Presentation)', resized_frame)

        # Display the video feed
        cv2.imshow('Gesture Detection', frame)

        if cv2.waitKey(1) & 0xFF == 27:  # Exit on 'Esc'
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
