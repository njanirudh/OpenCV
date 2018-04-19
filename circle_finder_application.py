import cv2
import numpy as np

class CircleFinderApplication:

    window_name = 'CircleFinder'

    input_img = None

    thresh_min = 20
    thresh_max = 20

    r_min = 0
    r_max = 300

    def __init__(self, t_min_init = 20 ,t_max_init = 30 , r_min_init = 120 , r_max_init = 150):
        cv2.namedWindow(self.window_name , cv2.WINDOW_FREERATIO)

        cv2.createTrackbar('t_min', self.window_name, 10, 255, self.update_min_threshold)
        cv2.createTrackbar('t_max', self.window_name, 10, 255, self.update_max_threshold)

        cv2.createTrackbar('r_min', self.window_name, 10, 500, self.update_min_radius)
        cv2.createTrackbar('r_max', self.window_name, 10 ,500 , self.update_max_radius)

        cv2.setTrackbarPos('t_min', self.window_name,t_min_init)
        cv2.setTrackbarPos('t_max', self.window_name,t_max_init)
        cv2.setTrackbarPos('r_min', self.window_name,r_min_init)
        cv2.setTrackbarPos('r_max', self.window_name,r_max_init)


    def process_image(self,input,wait = 30):
        output = self.run_circle_finder(input)
        cv2.imshow(self.window_name , output)
        cv2.waitKey(wait)

    def set_preprocessing(self,pre_processor):
        self.preprocessor = pre_processor
        pass

    def update_min_threshold(self,x):
        self.thresh_min = x

    def update_max_threshold(self, x):
        self.thresh_max = x

    def update_min_radius(self,x):
        self.r_min = x

    def update_max_radius(self,x):
        self.r_max = x

    def run_circle_finder(self,input):

        self.processed_image = input
        gray = cv2.cvtColor(self.processed_image,cv2.COLOR_RGB2GRAY)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 80,
                                   param1=self.thresh_min, param2=self.thresh_max,
                                   minRadius=self.r_min, maxRadius=self.r_max)
        try:
            for i in circles[0, :]:
                # draw the outer circle
                cv2.circle(self.processed_image, (i[0], i[1]), i[2], (255, 0, 0), 2)
                # draw the center of the circle
                cv2.circle(self.processed_image, (i[0], i[1]), 2, (0, 0, 255), 3)

            return self.processed_image

        except:
            return input

    def set_postprocessor(self, post_processor):
        pass


class Preprocessor:

    input_image = None
    processed_image = None

    def __init__(self):
        pass

    def preprocess_image(self,image):
        self.input_image = image
        self.processed_image = image

        pass

    def get_preprocessed_image(self):
        return self.processed_image

if __name__ == "__main__":

    cap = cv2.VideoCapture("/home/predator-nj/Pictures/plate/images/2018-04-03-162404.webm")
    circle_finder = CircleFinderApplication(100,150,200,250)

    while cap.isOpened():
        _, img = cap.read()
        w = img.shape[1]
        h = img.shape[0]

        #image = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        #image = cv2.resize(img, (0, 0), fx=0.50, fy=0.50)

        circle_finder.process_image(img)
