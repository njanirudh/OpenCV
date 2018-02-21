import cv2
from glob import glob
from os import path

def split_image(file_name):
    print(file_name)
    img = cv2.imread(file_name, cv2.IMREAD_UNCHANGED)
    image_width, image_height, image_channels = img.shape
    width_pieces = 2
    height_pieces = 2
    piece_width = image_width / width_pieces
    piece_height = image_height / height_pieces
    index = 0
    w_index = 0
    for w_itr in range(0, image_width, piece_width):
        h_index = 0
        for h_itr in range(0, image_height, piece_height):
            x1 = w_index * piece_width
            x2 = (w_index + 1) * piece_width
            y1 = h_index * piece_height
            y2 = (h_index + 1) * piece_height
            piece_i = img[x1:x2, y1:y2]
            base_file_name = path.basename(file_name)
            suffix_i = "_" + str(index) + ".jpg"
            base_file_name = base_file_name.replace(".JPG", suffix_i)
            out_file_name = path.dirname(file_name) + "/split/" + base_file_name
            print(out_file_name)
            cv2.imwrite(out_file_name, piece_i)
            h_index += 1
            index += 1
        w_index += 1

for file_name in glob('Images/pipes.jpg'):
    split_image(file_name)