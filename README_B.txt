# Hand Tracking and Finger Counting using OpenCV and MediaPipe

This project demonstrates real-time hand tracking and finger counting using OpenCV and MediaPipe. It detects up to two hands and counts the number of fingers held up for each hand.

## Features

- **Real-time Hand Tracking**: Uses MediaPipe to detect hands in a live video feed.
- **Finger Counting**: Counts the number of fingers held up for each detected hand.
- **Multiple Hands**: Supports detection of up to two hands simultaneously.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe

You can install the required dependencies with the following command:

```bash
pip install opencv-python mediapipe
```

## How to Run

1. Clone or download this project.
2. Connect your webcam or ensure it is accessible.
3. Run the Python script:
```bash
python b.py
```
4. The webcam feed will open and display the detected hands along with the number of fingers raised for each hand.
5. Press q to exit the program.

## Code Explanation
Hand Detection and Finger Counting

- MediaPipe: The script uses the MediaPipe Hands model to detect hand landmarks in real-time.
- Finger Counting: For each detected hand, the script checks the positions of key landmarks to determine if a finger is raised:
    - Thumb: Compared with the Interphalangeal (IP) and Metacarpophalangeal (MCP) joints.
    - Index, Middle, Ring, and Pinky fingers: Compared with their respective joints.
- Multiple Hands: The program can detect and count fingers for up to two hands simultaneously.

## Logic for Counting Fingers

The program tracks the following landmarks for each hand:

- Thumb: Checks if the thumb tip is higher than both the IP and MCP joints.
- Index Finger: Checks if the tip is higher than both the DIP and PIP joints.
- Middle Finger: Similar checks as the index finger.
- Ring Finger: Same approach as the other fingers.
- Pinky: Uses the same logic for tip versus joint comparison.

The total number of fingers held up is displayed on the screen for each hand.

## Example Output

The output will be the webcam feed with hand landmarks drawn and the number of fingers held up displayed for each detected hand.

## License

This project is open-source and available under the MIT License. See the LICENSE file for details.

## References

- OpenCV Documentation
- MediaPipe Hands Documentation