from skimage.feature import hessian_matrix, hessian_matrix_eigvals

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Images/h_pipes_Big.jpg", cv2.IMREAD_UNCHANGED)

Hessen = hessian_matrix(img, sigma=1.5)
i1, i2 = hessian_matrix_eigvals(Hessen[0], Hessen[1], Hessen[2])

# Visualise the result
plt.imshow(i2)
plt.show()

