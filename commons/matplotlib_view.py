import math

# Error in MAC
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

# Dynamic Image viewing in MatPlotLib
# Reads a dictionary of the format {"title" : <image mat>}
def view_image_list(imgList):
    rowNumber = int(math.ceil(imgList.__len__() / 2.0))
    fig, ax = plt.subplots(nrows=rowNumber, ncols=2)

    count = 0
    for key,val in imgList.items():
        try:
            plt.subplot(rowNumber, 2, count + 1).set_title(key)
            plt.imshow(val)
            plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

            count += 1

        except IndexError:
            print('Index doesnt exist')

    plt.show()

def viewSingleImage(input):
    plt.imshow(input)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

