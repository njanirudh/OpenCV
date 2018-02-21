import cv2

img = cv2.imread("Images/pipes.jpg",cv2.IMREAD_UNCHANGED)

gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
yuv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
ycrcb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

cv2.imshow("Gray", gray_frame)
cv2.imshow("HSV", hsv_frame)
cv2.imshow("YUV", yuv_frame)
cv2.imshow("YCrCb", ycrcb_frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
