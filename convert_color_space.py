import cv2
from commons import matplotlib_view

if __name__ == "__main__":
    IMAGE_PATH = "Images/color_wheel.jpg"

    img = cv2.imread(IMAGE_PATH,cv2.IMREAD_UNCHANGED)

    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    luv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
    hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    yuv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    ycrcb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    image_list = {}
    image_list["Normal"] = img

    image_list["LUV"] = luv_frame
    image_list["GRAY"] = gray_frame
    image_list["HSV"] = hsv_frame
    image_list["YUV"] = yuv_frame
    image_list["YCrCb"] = ycrcb_frame

    matplotlib_view.view_image_list(image_list)
