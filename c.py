import cv2
import mediapipe as mp

# Initialize MediaPipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5)

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)
    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and find hands
    results = hands.process(rgb_frame)

    # Initialize total finger count
    total_fingers = 0

    # Draw the hand annotations on the frame
    if results.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Count the number of fingers up for each hand
            count_fingers = 0
            landmarks = hand_landmarks.landmark
            
            # Thumb
            if landmarks[mp_hands.HandLandmark.THUMB_TIP].y < landmarks[mp_hands.HandLandmark.THUMB_IP].y and \
               landmarks[mp_hands.HandLandmark.THUMB_TIP].y < landmarks[mp_hands.HandLandmark.THUMB_MCP].y:
                count_fingers += 1

            # Index Finger
            if landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.INDEX_FINGER_DIP].y and \
               landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y:
                count_fingers += 1

            # Middle Finger
            if landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y and \
               landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y:
                count_fingers += 1

            # Ring Finger
            if landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.RING_FINGER_DIP].y and \
               landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.RING_FINGER_PIP].y:
                count_fingers += 1

            # Pinky
            if landmarks[mp_hands.HandLandmark.PINKY_TIP].y < landmarks[mp_hands.HandLandmark.PINKY_DIP].y and \
               landmarks[mp_hands.HandLandmark.PINKY_TIP].y < landmarks[mp_hands.HandLandmark.PINKY_PIP].y:
                count_fingers += 1

            # Add to total fingers
            total_fingers += count_fingers

            # Display the number of fingers for each hand
            cv2.putText(frame, f'Hand {idx + 1} Fingers: {count_fingers}', (10, 70 + idx * 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display total fingers up to 10
    cv2.putText(frame, f'Total Fingers: {total_fingers}', (10, 150), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)

    cv2.imshow("Hand Tracking", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
