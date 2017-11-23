# OpenCV
This repository has small scripts showing the working of the various functions in OpenCV .

### Image Color-Space conversion (convert_color_space.py)

* OpenCV has the functionality to change the color space of the image into the Gray, HSV , YUV ,YCrCb etc.
Changing color spaces is  helpful specially when the Image processing logic uses some kind of color segmentation or blob detection. 

### Difference of Gaussian (difference_of_gaussian.py)

* Difference of gaussian involves finding the difference  of one blurred version of an original image from another, less blurred version of the original . DoG method can be used for edge detection.

* When using DoG method change the kernal size of the two gaussian blurs to check which gives the best edge for a given image.    

### Circle Finder 

* Circle finder makes use of the [Hough Circle Transform](https://en.wikipedia.org/wiki/Circle_Hough_Transform) Algorithm to find circles in the images.

* Set the parameters of minimum radius and maximum radius to find circle of different sizes.



