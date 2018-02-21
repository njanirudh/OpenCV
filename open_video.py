import numpy as np
import cv2


if __name__ == "__main__":

    # Video path here
    VIDEO_PATH = 'vtest.avi'
    cap = cv2.VideoCapture('vtest.avi')

    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()