# Hand Tracking and Total Finger Counting using OpenCV and MediaPipe

This project demonstrates real-time hand tracking and finger counting using OpenCV and MediaPipe. It detects up to two hands simultaneously, counts the number of fingers raised for each hand, and displays the total number of fingers up.

## Features

- **Real-time Hand Tracking**: Uses the MediaPipe Hands model to detect and track hand landmarks in a live video feed.
- **Finger Counting**: Counts the number of fingers raised on each hand and displays the total count.
- **Multiple Hands**: Supports detecting up to two hands and provides individual counts for each.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe

Install the required packages using:

```bash
pip install opencv-python mediapipe
```

## How to Run the Project

1. Clone this repository or download the Python script.
2. Ensure your webcam is connected.
3. Run the Python script:
```bash
python c.py
```

4. A window will open showing the webcam feed with hand landmarks and the number of fingers raised on each hand. The total number of fingers is also displayed.
5. Press q to exit the program.

## Code Explanation

- Hand Detection: The MediaPipe Hands model is initialized to detect up to two hands with a minimum confidence threshold of 0.5.
- Finger Counting Logic:
    - For each detected hand, the position of key hand landmarks is checked to determine if each finger is raised.
    - The thumb is considered raised if its tip is higher than its joints (IP and MCP).
    - Similarly, the index, middle, ring, and pinky fingers are checked by comparing the tip position with their joints (DIP and PIP).
- Total Finger Count: The number of fingers raised for both hands is summed and displayed on the screen.

## Example Output

The output will be the webcam feed with:

- The number of fingers raised for each detected hand.
- The total number of fingers up (up to 10 fingers for two hands).

## Screenshot

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## References

- OpenCV Documentation
- MediaPipe Hands Documentation