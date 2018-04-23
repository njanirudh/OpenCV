import cv2

class CannyDetectionApplication:

    window_name = 'Canny Detection'

    threshold_low = 20
    threshold_high = 20

    kernal = 3

    def __init__(self, t_min_init = 20 ,t_max_init = 130 , kernal = 3 ):
        cv2.namedWindow(self.window_name , cv2.WINDOW_FREERATIO)

        cv2.createTrackbar('t_low' , self.window_name, 10, 255, self.update_threshold_low)
        cv2.createTrackbar('t_high', self.window_name, 10, 255, self.update_threshold_high)
        cv2.createTrackbar('kernal', self.window_name, 1, 9, self.update_kernal)

        cv2.setTrackbarPos('t_low', self.window_name,t_min_init)
        cv2.setTrackbarPos('t_high', self.window_name,t_max_init)
        cv2.setTrackbarPos('kernal', self.window_name,kernal)

    def process_image(self,input,wait = 30 , preprocessor = None , postprocessor = None):

        main_image = input
        if(preprocessor != None):
            main_image = preprocessor.preprocess_image(input)

        main_image = self.run_canny_detection(main_image)

        if (postprocessor != None):
            pass

        cv2.imshow(self.window_name , main_image)
        cv2.waitKey(wait)

    def update_threshold_low(self,x):
        self.threshold_low = x

    def update_threshold_high(self, x):
        self.threshold_high = x

    def update_kernal(self,x):
        self.kernal = x

    def run_canny_detection(self,input):
        self.processed_image = input
        input = cv2.Canny(input,self.threshold_low,self.threshold_high,self.kernal)

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

    cap = cv2.imread("Images/sudoku.png")
    canny_detection = CannyDetectionApplication(100,150,3)

    while(1):
        canny_detection.process_image(cap,30)