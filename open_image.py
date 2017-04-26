import cv2

img = cv2.imread("C:/Users/ANIRUDH/Downloads/pipes.jpg",cv2.IMREAD_UNCHANGED)

#prints width,height,channels
print (img.shape)

#print total pixels
print (img.size)

#Show the image in the window
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

