import cv2
import numpy as np

# Error in MAC
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


def cannyEdgeDetection(image, min_val , max_val , aperture_size = 3):

    edges = cv2.Canny(image, min_val, max_val , aperture_size)
    return edges


def viewImage(img):
    plt.imshow(img, cmap=plt.get_cmap('gray'))
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()


if __name__ == "__main__":
    image_path = 'Images/color_wheel.jpg'
    processed_image = cv2.imread(image_path)

    processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
    processed_image = cannyEdgeDetection(processed_image , 50, 250)

    viewImage(processed_image)
