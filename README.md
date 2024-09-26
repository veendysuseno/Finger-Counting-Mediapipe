# Hand Tracking and Finger Counting using OpenCV and MediaPipe

This project demonstrates a simple application for hand tracking and finger counting using OpenCV and MediaPipe. The program captures a video feed from your webcam, detects your hand, and counts the number of fingers being held up.

## Features

- Real-time hand tracking using MediaPipe's Hands solution.
- Finger counting based on the position of hand landmarks.
- Live video display with hand annotations and finger count.

## Requirements

Make sure you have the following dependencies installed:

- Python 3.x
- OpenCV
- MediaPipe

You can install the required dependencies using the following command:

```bash
pip install opencv-python mediapipe
```

## How to Run

1. Clone this repository or download the script.
2. Ensure your webcam is connected or available.
3. Run the script using Python:
```bash
python a.py
```
4. The webcam feed will open, showing a live display of your hand with landmarks and the number of fingers being counted.
5. Press q to exit the program.

## Code Overview

- Hand Tracking: MediaPipe is used to detect hand landmarks in real-time.
- Finger Counting: The program compares the y-coordinates of the finger tips and their lower joints to determine whether a finger is raised or not.
- Display: OpenCV is used to display the hand landmarks and the current number of fingers raised.

## Main Libraries Used

- OpenCV: For capturing the video from the webcam and displaying the video feed.
- MediaPipe: To track the hand and detect finger positions through landmarks.

## Finger Counting Logic

The program checks the y-coordinates of the following finger landmarks:

- Thumb: THUMB_TIP, THUMB_IP, and THUMB_MCP
- Index Finger: INDEX_FINGER_TIP, INDEX_FINGER_DIP, and INDEX_FINGER_PIP
- Middle Finger: MIDDLE_FINGER_TIP, MIDDLE_FINGER_DIP, and MIDDLE_FINGER_PIP
- Ring Finger: RING_FINGER_TIP, RING_FINGER_DIP, and RING_FINGER_PIP
- Pinky: PINKY_TIP, PINKY_DIP, and PINKY_PIP

If the tip of a finger is higher (lower y value) than its middle joints, that finger is considered "up."

## Example Output

Once the program is running, the webcam will show the live video feed, tracking your hand and counting the fingers. The number of fingers will be displayed on the screen.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## References

- OpenCV Documentation 
- MediaPipe Hands Documentation