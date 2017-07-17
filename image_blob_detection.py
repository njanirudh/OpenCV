import cv2
import numpy as np

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt



def colorSegmentation(lower_bound, upper_bound, image):
    lower = np.array(lower_bound, dtype="uint8")
    upper = np.array(upper_bound, dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    return output


def viewImage(img):
    plt.imshow(img, cmap=plt.get_cmap('gray'))
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()


if __name__ == "__main__":
    image_path = 'Images/color_wheel.jpg'
    bgr_img = cv2.imread(image_path)

    hsv_frame = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
    segmented_image = colorSegmentation([0, 100, 100], [10, 255, 255], hsv_frame)

    viewImage(segmented_image)
