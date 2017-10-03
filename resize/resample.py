import cv2
import numpy as np
import math
from resize import interpolation

class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here
        width, height = image.shape
        print(width)
        print(height)

        newW = int(float(fx) * width)
        newH = int(float(fy) * height)
        print(newW,newH)

        ima = np.zeros((newW, newH))

        for i in range(0, newW):
            for j in range(0, newH):

                x = int(round(float(i) / float(newW) * float(width)))
                y = int(round(float(j) / float(newH) * float(height)))
                x = min(x, width - 1)
                y = min(y, height - 1)
                ima[i][j] = image[x][y]

        return ima


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here
        width, height = image.shape
        print(width)
        print(height)

        newW = int(float(fx) * width)
        newH = int(float(fy) * height)
        print(newW, newH)

        ima = np.zeros((newW, newH))

        inter = interpolation

        for i in range(0, newW):
            for j in range(0, newH):
                
                a = (i / newW)
                b = (j / newH)

                x = math.floor(a * width)
                y = math.floor(b * height)

                NW = image[x][y]
                NE = image[x ][y+1]
                SW = image[x+1][y ]
                SE = image[x+1][y + 1]

                uI = (b * height) - y
                uJ = (a * width) - x


                result = inter.bilinear_interpolation(NW, NE, SW, SE, (uI,uJ))

                ima[i][j] = result

        return ima

