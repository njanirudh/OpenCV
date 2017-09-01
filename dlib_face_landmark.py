import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from imutils import face_utils

import dlib
import cv2

def grab_frame(cap):
    ret,frame = cap.read()

    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # detect faces in the grayscale frame
    rects = detector(frame, 0)
    # loop over the face detections
    for rect in rects:
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(frame, rect)
        shape = face_utils.shape_to_np(shape)

        # loop over the (x, y)-coordinates for the facial landmarks
        # and draw them on the image
        for (x, y) in shape:
            cv2.circle(frame, (x, y), 5, (0, 255, 255), -1)

    return frame

#Initiate the two cameras
cap1 = cv2.VideoCapture(0)

print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


im1 = plt.imshow(grab_frame(cap1))

def update(i):
    im1.set_data(grab_frame(cap1))




ani = FuncAnimation(plt.gcf(), update, interval=25)
plt.show()