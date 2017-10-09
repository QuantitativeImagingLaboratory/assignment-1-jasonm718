import matplotlib.pyplot as plt
import cv2
import numpy as np

class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""

        w, h = image.shape

        regions = dict()
        k = 1

        R = np.zeros((w, h), dtype=np.uint32)

        for i in range(0,w):

            for j in range(0,h):
                #print(regions)
               # if (R[i, j - 1] == 0 or R[i - 1, j] == 0):

                #print(i, j, R[i, j - 1], R[i - 1, j], image[i, j], image[i - 1, j], image[i, j - 1])

                if(image[i][j] == 255 and image[i][j-1]== 0 and image[i-1][j] == 0):
                    R[i,j] = k
                    regions[k] = [(i,j)]
                    k += 1

                elif(image[i][j] == 255 and image[i][j-1] == 0 and image[i-1][j] == 255):
                    R[i, j] = R[i-1, j]
                    regions[R[(i, j)]].append((i, j))

                elif (image[i][j] == 255 and image[i][j-1] == 255 and image[i-1][j] == 0):

                    R[i, j] = R[i, j - 1]
                    regions[R[i, j]].append((i, j))

                elif (image[i][j] == 255 and image[i][j-1] == 255 and image[i-1][j] == 255):
                    R[i, j] = R[i-1, j]

                    if R[i, j - 1] != R[i - 1, j]:
                        R[i,j-1] = R[i-1,j]

                    regions[R[i, j]].append((i, j))

        print(regions.keys())
        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""



        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return 0

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        plt.clf()
        plt.imshow(image, interpolation= 'none', cmap=plt.cm.gray)

        plt.show()
        plt.savefig('output/cellct/result.png')

        return image

