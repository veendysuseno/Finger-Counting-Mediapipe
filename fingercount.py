import cv2
import numpy as np
import os

# Load the names of classes
with open("model/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Load YOLO
net = cv2.dnn.readNet("model/yolov3-tiny.weights", "model/yolov3-tiny.cfg")

# Get the output layer names
layer_names = net.getLayerNames()
unconnected_layers = net.getUnconnectedOutLayers()
output_layers = [layer_names[i - 1] for i in unconnected_layers.flatten()]

# Start video capture
cap = cv2.VideoCapture(0)

def count_fingers(hand_region):
    # Convert to grayscale
    gray = cv2.cvtColor(hand_region, cv2.COLOR_BGR2GRAY)
    # Apply GaussianBlur
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)
    # Apply thresholding
    _, thresh = cv2.threshold(blurred, 50, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        return 0

    # Find the largest contour
    max_contour = max(contours, key=cv2.contourArea)
    # Calculate the convex hull
    hull = cv2.convexHull(max_contour)
    # Calculate the convexity defects
    defects = cv2.convexityDefects(max_contour, cv2.convexHull(max_contour, returnPoints=False))

    # Count defects
    finger_count = 0
    if defects is not None:
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i][0]
            # Calculate the distance of the defect point to the convex hull
            if d > 100:  # Tuning threshold for counting fingers
                finger_count += 1

    return finger_count + 1  # Add one for the base finger

while True:
    success, img = cap.read()
    if not success:
        print("Gagal menangkap gambar.")
        break

    # Detect objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    # Process outputs
    boxes, confidences, class_ids = [], [], []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Tuning threshold
                center_x = int(detection[0] * img.shape[1])
                center_y = int(detection[1] * img.shape[0])
                w = int(detection[2] * img.shape[1])
                h = int(detection[3] * img.shape[0])
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Non-max suppression
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    total_fingers = 0  # Initialize total fingers count

    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            label = classes[class_ids[i]]  # Use class names instead of IDs
            cv2.putText(img, label, (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

            # Check if the detected class is a hand
            if label == "hand":  # Change "hand" to the appropriate class name for hands in your model
                # Crop the hand region from the image
                hand_region = img[y:y+h, x:x+w]
                # Count the fingers in the hand region
                total_fingers += count_fingers(hand_region)

    # Display total fingers on the image
    cv2.putText(img, f'Total Fingers: {total_fingers}', (10, 70), 
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)

    cv2.imshow("Image", img)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
