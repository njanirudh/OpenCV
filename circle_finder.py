import cv2

def findCircle(circleImg):

    grayscale_img = cv2.cvtColor(circleImg, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(grayscale_img,(640,480),interpolation= cv2.INTER_AREA )

    blurred_img = cv2.medianBlur(resized_image,5 )

    circles = cv2.HoughCircles(blurred_img, cv2.HOUGH_GRADIENT, 1, 100,
                               param1=50, param2=50, minRadius=40, maxRadius=200)

    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(blurred_img, (i[0], i[1]), i[2], (255, 0, 0), 2)
        # draw the center of the circle
        cv2.circle(blurred_img, (i[0], i[1]), 2, (0, 0, 255), 3)

    color_img = cv2.cvtColor(blurred_img,cv2.COLOR_GRAY2RGB)

    cv2.imshow("Image", color_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":

    IMAGE_PATH = "Images/pipes.jpg"

    img = cv2.imread(IMAGE_PATH, cv2.IMREAD_UNCHANGED)
    findCircle(img)
