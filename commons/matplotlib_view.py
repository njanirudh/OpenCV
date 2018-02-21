import math

# Error in MAC
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

# Dynamic Image viewing in MatPlotLib
def viewImageList(imgList):
    rowNumber = int(math.ceil(imgList.__len__() / 2.0))
    fig, ax = plt.subplots(nrows=rowNumber, ncols=2)

    for i in range(0, imgList.__len__()):
        try:
            plt.subplot(rowNumber, 2, i + 1)
            plt.imshow(imgList[i])
            plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis

        except IndexError:
            print('Index doesnt exist')

    plt.show()

def viewSingleImage(input):
    plt.imshow(input)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

