import numpy as np
from PIL import Image as pilImage

class SubImageLibrary(object):
    def get_sub_image(self, img_path, x1, x2, y1, y2):
        # Get the image and covert it to a PIL image

        # Select and return the section as
        # given by (x1, x2, y1, y2)


    def match_images(self, img_path, sub_img_path, scales, threshod):
        # Get original images and convert to PIL & grayscale images

        # According to the scales, make a pyramid to
        # present the input image in different sizes

        # Resize the sub_image to detect, and use a Gaussian filter
        # to smooth out the artifacts caused by downsizing

        # loop through each of the windows on the input image, and
        # apply normalized cross-correlation to find the best match

        # return the best match, and also information about
        # if the best match has similarity >= threshod
