import cv2
import numpy as np
import math

# Error in MAC
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


def brg2rgb(bgr_img):
    b, g, r = cv2.split(bgr_img)  # get b,g,r
    rgb_img = cv2.merge([r, g, b])  # switch it to rgb

    return rgb_img


def thresholdimage(image):
    image = cv2.cvtColor(orignalImage, cv2.COLOR_RGB2GRAY)
    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    return image

def sobleFilter(image):
    gx = cv2.Sobel(image, cv2.CV_32F, 1, 0, ksize=1)
    gy = cv2.Sobel(image, cv2.CV_32F, 0, 1, ksize=1)

    return gx,gy

def cannyEdgeDetection(image, min_val=10, max_val=100, aperture_size=3):
    edges = cv2.Canny(image, min_val, max_val, aperture_size)
    return edges


def differenceOfGaussian(img, kernal1=(9, 9), kernal2=(1, 1)):
    blur1 = cv2.GaussianBlur(img, kernal1, 0)
    blur2 = cv2.GaussianBlur(img, kernal2, 0)

    DoGim = blur1 - blur2

    return DoGim


def binarizeImage(image):
    # load the image and perform pyramid mean shift filtering
    # to aid the thresholding step
    shifted = cv2.pyrMeanShiftFiltering(image, 21, 51)

    # convert the mean shift image to grayscale, then apply
    # Otsu's thresholding
    gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255,
                           cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    return thresh


def cleanImageNoise(image, iterations):
    for i in range(0, iterations):
        image = cv2.medianBlur(image, 3)
        image = cv2.bilateralFilter(image, 9, 75, 75)

    return image


# Dynamic Image viewing in MatPlotLib
def viewImageList(imgList):
    rowNumber = int(math.ceil(imgList.__len__() / 2.0))
    fig, ax = plt.subplots(nrows=rowNumber, ncols=2)

    for i in range(0, imgList.__len__()):
        try:
            plt.subplot(rowNumber, 2, i + 1)
            plt.imshow(imgList[i])
            plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

        except IndexError:
            print('Index doesnt exist')

    plt.show()


def findContours(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # image = cv2.threshold(image, 100, 255, 0)

    im2, contours, hierarchy = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 0, 180), 1)

    return image


def lineDetect(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    #lines = cv2.HoughLines(image, 1, np.pi / 180, 200)
    lines = cv2.HoughLinesP(image, rho=1, theta=np.pi / 180, threshold=20, minLineLength=20, maxLineGap=300)
    print(lines[0])

    for x1, y1, x2, y2 in lines[0]:
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)




if __name__ == "__main__":
    imgList = []
    image_path = 'Images/h_pipes_Big.jpg'

    orignalImage = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # cleanedImage = cv2.cvtColor(orignalImage, cv2.cv2.COLOR_BRG2)
    # imgList.append(cleanedImage)

    cleanedImage = brg2rgb(orignalImage)
    imgList.append(cleanedImage)

    cleanedImage = cleanImageNoise(cleanedImage, 1)
    #imgList.append(cleanedImage)


    processed_image = differenceOfGaussian(cleanedImage, (9, 9), (5, 5))
    imgList.append(processed_image)

    processed_image = cv2.dilate(processed_image ,(5,5))
    imgList.append(processed_image)

    processed_image = cv2.erode(processed_image ,(5,5))
    imgList.append(processed_image)

    # processed_image = cv2.dilate(processed_image ,(5,5))
    # imgList.append(processed_image)

    #processed_image = cannyEdgeDetection(processed_image)
    #imgList.append(processed_image)

    lineDetect(processed_image)

    viewImageList(imgList)

