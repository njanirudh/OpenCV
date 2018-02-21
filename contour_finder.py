import cv2
import matplotlib.pyplot as plt
from commons.matplotlib_view import viewImageList


if __name__ == "__main__":
    IMAGE_PATH = "Images/pipes.jpg"

    source_image = cv2.imread(IMAGE_PATH)
    gray_image = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)

    for threshold_itr in range(25, 100, 25):
        print("Current image threshold = " + str(threshold_itr))
        ret, thresh = cv2.threshold(gray_image, threshold_itr, 255, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(source_image, contours, -1, (0, 0, 180), 3)

    plt.imshow(source_image)

    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()


