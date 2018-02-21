import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread("Images/h_pipes_Big.jpg",cv2.IMREAD_UNCHANGED)

for i in range(0,1):
    img = cv2.medianBlur(img,3)
    img = cv2.bilateralFilter(img,9,75,75)

# Performing two different Gaussian blurs on the image,
# with a different blurring radius for each,
# and subtracting them to yield the result.
blur_high = cv2.GaussianBlur(img, (9, 9), 0)
blur_low = cv2.GaussianBlur(img, (1, 1), 0)

DoG_img = blur_high - blur_low

plt.imshow(DoG_img)
plt.xticks([]), plt.yticks([])   # to hide tick values on X and Y axis
plt.show()
