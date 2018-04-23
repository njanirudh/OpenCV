import cv2
from skimage.feature import hessian_matrix, hessian_matrix_eigvals


def get_hessian_matrix(input):

    Hessen = hessian_matrix(input, sigma=1.5)
    eigen1, eigen2 = hessian_matrix_eigvals(Hessen[0], Hessen[1], Hessen[2])

    return eigen1 , eigen2


if __name__ == "__main__":

    img = cv2.imread("Images/h_pipes_Big.jpg", cv2.IMREAD_UNCHANGED)

    eigen1 , eigen2 = get_hessian_matrix(img)
    cv2.imshow("Lower Eigen-Value",eigen1)
    cv2.imshow("Higher Eigen-Value",eigen2)

    cv2.waitKey(0)