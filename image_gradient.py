import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread('Images/pipes.jpg')
img = np.float32(img) / 255.0

# Calculate gradient
gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=1)
gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=1)

mag, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)


plt.imshow(mag)

plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

