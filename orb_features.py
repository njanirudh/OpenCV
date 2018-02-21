import numpy as np
import cv2
from commons import matplotlib_view

if __name__ == "__main__":

    IMAGE_PATH = 'Images/h_pipes_Big.jpg'
    img = cv2.imread(IMAGE_PATH,0)

    # Initiate ORB detector
    orb = cv2.ORB_create()

    # find the keypoints with ORB
    kp = orb.detect(img,None)

    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)

    # draw only keypoints location,not size and orientation
    out = np.zeros(shape=[img.shape[0],img.shape[1]])
    kp_image = cv2.drawKeypoints(img,kp,out)

    matplotlib_view.viewSingleImage(kp_image)