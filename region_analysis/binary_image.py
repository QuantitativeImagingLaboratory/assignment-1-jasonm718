import numpy as np
import matplotlib.pyplot as plt

import cv2

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        w,h = image.shape

        #List created with 256 values of 0
        hist = [0]*256

        #For loop created to record the amount of times a certain pixel value was reached
        for x in range(0,w):
            for y in range(0,h):
                pixelV = image[x][y]
                hist[pixelV] += 1

        #returns list of values for the histogram
        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        #threshold = 0

        threshold = int(len(hist)/2)    #threshold set to the middle X of the Histogram
        pixels = sum(hist)  #number of pixels

        (upper, prev) = (0,0)

        x = binary_image.expected_value(self, hist[:threshold],0,pixels)
        y = binary_image.expected_value(self, hist[threshold:],threshold, pixels)
        threshold = int((x+y)/2)#average between peeks
        (du, dv) = (x-upper, y-prev)

        while du != 0 and dv !=0:

            (upper,prev) = (x,y)
            x = binary_image.expected_value(self,hist[:threshold], 0, pixels)
            y = binary_image.expected_value(self,hist[threshold:], threshold, pixels)
            threshold = int((x + y) / 2) #average between peeks
            (du, dv) = (x - upper, y - prev)

        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""
        w, h = image.shape
        bin_img = image.copy()
        hist = binary_image.compute_histogram(self,image)
        t = binary_image.find_optimal_threshold(self, hist)

        for i in range(w):
            for j in range(h):
                if(image[i][j] <=t):
                    bin_img[i][j] = 0
                else:
                    bin_img[i][j] = 255

        return bin_img

    def expected_value(self, pdf, ini, pixels):
        exp = 0
        for i,val in enumerate(pdf):
            exp += (i+ini)* val/pixels

        return exp


