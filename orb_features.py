import numpy as np
import cv2
from commons import matplotlib_view

if __name__ == "__main__":

    IMAGE_PATH = 'Images/pipes.jpg'
    img = cv2.imread(IMAGE_PATH,0)

    # Initiate ORB detector
    orb = cv2.ORB_create()

    # find the keypoints with ORB
    kp = orb.detect(img,None)

    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)

    # draw only keypoints location,not size and orientation

    out = np.zeros(shape=[720,960])
    img2 = cv2.drawKeypoints(img,kp,out)
    matplotlib_view.singleImageView(img2)