import cv2
import matplotlib.pyplot as plt


if __name__ == "__main__":

    IMAGE_PATH = 'Images/pipes.jpg'

    bgr_img = cv2.imread(IMAGE_PATH)

    b,g,r = cv2.split(bgr_img)       # get b,g,r
    rgb_img = cv2.merge([r,g,b])     # switch it to rgb

    plt.imshow(rgb_img)
    plt.xticks([]), plt.yticks([])   # to hide tick values on X and Y axis
    plt.show()
