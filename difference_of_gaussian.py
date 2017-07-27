import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread("Images/h_pipes_4.jpg",cv2.IMREAD_UNCHANGED)

for i in range(0,1):
    img = cv2.medianBlur(img,5)
    img = cv2.bilateralFilter(img,9,75,75)
    #img = cv2.dilate(img,(3,3))

blur5 = cv2.GaussianBlur(img, (9, 9), 0)
blur3 = cv2.GaussianBlur(img, (1, 1), 0)

DoGim = blur5 - blur3

#DoGim = cv2.erode(DoGim,(3,3))
#DoGim = cv2.cvtColor(DoGim,cv2.COLOR_BGR2GRAY)

plt.imshow(DoGim)
plt.xticks([]), plt.yticks([])   # to hide tick values on X and Y axis
plt.show()
