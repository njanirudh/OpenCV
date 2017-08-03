import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def grab_frame(cap):
    ret,frame = cap.read()
    return cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

#Initiate the two cameras
cap1 = cv2.VideoCapture(0)

im1 = plt.imshow(grab_frame(cap1))

def update(i):
    im1.set_data(grab_frame(cap1))

ani = FuncAnimation(plt.gcf(), update, interval=25)
plt.show()