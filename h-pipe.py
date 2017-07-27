from skimage.feature import hessian_matrix, hessian_matrix_eigvals
import cv2

img = cv2.imread("Images/pipes.jpg",cv2.IMREAD_UNCHANGED)

#assume you have an image img

hxx, hxy, hyy = hessian_matrix(img, sigma=3)
i1, i2 = hessian_matrix_eigvals(hxx, hxy, hyy)

#i2 is the variable you want.

#Visualise the result
import matplotlib.pyplot as plt
plt.imshow(i2)