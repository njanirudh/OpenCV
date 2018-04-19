import cv2
import numpy
from commons import matplotlib_view
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

    out_img_9 = DifferenceOfGaussian(img, (9,9), (1,1))
    out_img_5 = DifferenceOfGaussian(img, (5,5), (1,1))
    out_img_3 = DifferenceOfGaussian(img, (3,3), (1,1))

    image_list = {}
    image_list["Normal"] = img
    image_list["Gaussian 9x9"] = out_img_9
    image_list["Gaussian 5x5"] = out_img_5
    image_list["Gaussian 3x3"] = out_img_3

    matplotlib_view.view_image_list(image_list)
