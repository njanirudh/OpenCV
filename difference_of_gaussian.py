import cv2
import numpy
import matplotlib.pyplot as plt

def DifferenceOfGaussian(input , kernal_high , kernal_low):
    # Performing two different Gaussian blurs on the image,
    # with a different blurring radius for each,
    # and subtracting them to yield the result.
    blur_high = cv2.GaussianBlur(input, kernal_high, 0)
    blur_low = cv2.GaussianBlur(input, kernal_low, 0)

    DoG_img = blur_high - blur_low

    return DoG_img

if __name__ == "__main__":
    IMAGE_PATH = "Images/h_pipes_Big.jpg"

    img = cv2.imread(IMAGE_PATH,cv2.IMREAD_UNCHANGED)

    for i in range(0,1):
        img = cv2.medianBlur(img,3)
        img = cv2.bilateralFilter(img,9,75,75)

    out_img = DifferenceOfGaussian(img, (9,9), (1,1))

    plt.imshow(out_img)
    plt.xticks([]), plt.yticks([])   # to hide tick values on X and Y axis
    plt.show()
