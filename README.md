<img src="https://cdn-images-1.medium.com/max/428/1*5bSooyDhHPPSsarNzBQr1w.png" width="150">    

# OpenCV
This repository has small scripts showing the working of the various functions in OpenCV .

## Scripts

### Image BGR to RGB (bgr2rgb.py)

* OpenCV opens an image in the [BGR format](https://www.learnopencv.com/why-does-opencv-use-bgr-color-format/). So it is important to convert it into RGB format to make it compatible with other libraries.

### Open an Image (open_image.py)

* Script to open an image using OpenCV and find the various image dimensions and properties.

### Video Capture (video_capture.py)

* Script to capture a video stream from the webcam and perform some image processing operation on it.

### Kalman Filter on a moving point (kalman_filter.py)

### Image Color-Space conversion (convert_color_space.py)

* OpenCV has the functionality to change the color space of the image into the Gray, HSV , YUV ,YCrCb etc.
Changing color spaces is helpful specially when the Image processing logic uses some kind of color segmentation or blob detection. 

### Difference of Gaussian (difference_of_gaussian.py)

* Difference of Gaussian (DoG) involves finding the difference of one blurred version of an original image from another, less blurred version of the original . DoG method can be used for edge detection.

* When using DoG method change the kernal size of the two gaussian blurs to check which gives the best edge for a given image.    

### Circle Finder (circle_finder_application.py)

* Circle finder makes use of the [Hough Circle Transform](https://en.wikipedia.org/wiki/Circle_Hough_Transform) algorithm to find circles in the images.

* Set the parameters of minimum radius and maximum radius to find circle of different sizes.

### ORB feature extraction (orb_features.py)

* ORB ([Oriented FAST and rotated BRIEF](https://en.wikipedia.org/wiki/Oriented_FAST_and_rotated_BRIEF))

### Contour Finder (contour_finder.py)

### Hessian of an Image (hessian_image.py)

### Stereo Depth (stereo_depth.py)

### Image Gradients using Sobel filters (image_gradient.py)