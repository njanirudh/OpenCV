import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def update(im1):
    im1.set_data(frame)


if __name__ == "__main__":

    cap = cv2.VideoCapture(0)

    #Initiate the two cameras
    while(1):

        ret,frame = cap.read()

        im1 = plt.imshow(frame)

        video = FuncAnimation(plt.gcf(), update, interval=25)
        plt.show()