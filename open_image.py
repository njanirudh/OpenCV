import cv2


if __name__ == "__main__":

    IMAGE_PATH = 'Images/pipes.jpg'

    img = cv2.imread(IMAGE_PATH,cv2.IMREAD_UNCHANGED)

    #prints width,height,channels
    print (img.shape)

    #print total pixels
    print (img.size)

    #Show the image in the window
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

