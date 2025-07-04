import cv2
import numpy as np
import math

lowerBound = np.array([0, 0, 0])
upperBound = np.array([0, 0, 255])

cam = cv2.VideoCapture("debris.mp4")
if not cam.isOpened():
    print("Error: Cannot open video file.")
    exit()

kernelOpen = np.ones((5, 5), np.uint8)
kernelClose = np.ones((20, 20), np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX

next_object_id = 1
tracked_objects = {}         
counted_ids = set()          

count_small = 0
count_medium = 0
count_large = 0

def get_centroid(x, y, w, h):
    return (int(x + w / 2), int(y + h / 2))

def euclidean_distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

while True:
    ret, img = cam.read()
    if not ret or img is None:
        break

    img = cv2.resize(img, (1366, 768))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHSV, lowerBound, upperBound)
    maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

    contours, _ = cv2.findContours(maskClose.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    updated_objects = {}

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 500:
            continue

        x, y, w, h = cv2.boundingRect(cnt)
        centroid = get_centroid(x, y, w, h)

        matched_id = None
        for obj_id, prev_centroid in tracked_objects.items():
            if euclidean_distance(centroid, prev_centroid) < 50:
                matched_id = obj_id
                break

        if matched_id is None:
            matched_id = next_object_id
            next_object_id += 1

            if area < 1500:
                count_small += 1
            elif area < 4000:
                count_medium += 1
            else:
                count_large += 1

            counted_ids.add(matched_id)

        updated_objects[matched_id] = centroid

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, f"ID:{matched_id}", (x, y - 10), font, 0.6, (0, 255, 255), 2)

    tracked_objects = updated_objects

    cv2.putText(img, f"Small: {count_small}", (20, 40), font, 1, (0, 255, 0), 2)
    cv2.putText(img, f"Medium: {count_medium}", (20, 80), font, 1, (0, 255, 255), 2)
    cv2.putText(img, f"Large: {count_large}", (20, 120), font, 1, (0, 0, 255), 2)

    watermark = "Made by Aditya Tiwari"
    text_size = cv2.getTextSize(watermark, font, 1, 2)[0]
    text_x = img.shape[1] - text_size[0] - 20
    text_y = img.shape[0] - 20
    cv2.putText(img, watermark, (text_x, text_y), font, 1, (200, 200, 200), 2)

    cv2.imshow("Space Debris Detection", img)

    key = cv2.waitKey(10)
    if key == 27: 
        break

cam.release()
cv2.destroyAllWindows()

print("\n--- Final Unique Debris Count ---")
print(f"Small Debris: {count_small}")
print(f"Medium Debris: {count_medium}")
print(f"Large Debris: {count_large}")
