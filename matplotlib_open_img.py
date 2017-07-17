# View a cv2 image in matplotlib

import cv2
import matplotlib.pyplot as plt

image_path = 'Images/pipes.jpg'

bgr_img = cv2.imread(image_path)
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray_img, cmap = plt.get_cmap('gray'))
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

while True:
    k = cv2.waitKey(0) & 0xFF    # 0xFF? To get the lowest byte.
    if k == 27: break            # Code for the ESC key

cv2.destroyAllWindows()
