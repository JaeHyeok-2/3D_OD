import cv2 
from tracker import *


# Crate Tracker Object 
tracker = EuclideanDistTracker()


cap = cv2.VideoCapture("highway.mp4")


# 특정 부분의 ROI만 확인

#Object Detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)


while True:
    ret, frame = cap.read()

    height, width, _ = frame.shape 


    # Extract Region of Interest 
    roi = frame[300:720, 500:850]



    # 1. Object Detection 
    mask = object_detector.apply(roi)
    # Remove Shadow : 흰색만이 우리가 원하는 Object
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY) 
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:  
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 100 : 
            # cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
            x, y, w, h = cv2.boundingRect(cnt)

            
            detections.append([x, y, w, h])

    # 2. Object Tracking 
    boxes_ids = tracker.update(detections)
    print(boxes_ids)


    for box_id in boxes_ids : 
        x, y, w, h, id = box_id 
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)
        



    # Show Video 

    cv2.imshow('ROI', roi)
    cv2.imshow("Frame", frame) 
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(25)
    if key == ord('q'):
        break

cap.release()
cv2.destoryAllWindows()