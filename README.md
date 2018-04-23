# OpenCV
This repository has small scripts showing the working of the various functions in OpenCV .

## Scripts

### Open an Image (open_image.py)

### Video Capture (video_capture.py)

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

### Contour Finder (contour_finder.py)

### Hessian of an Image (hessian_image.py)

### Stereo Depth (stereo_depth.py)
