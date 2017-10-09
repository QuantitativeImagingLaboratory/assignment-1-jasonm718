1) Resampling

First i figured out how to do nearest neighbor. Then proceeded to linear interpolation. Bilinear interpolation was just
the linear interpolation of two linear interpolations. Basically, followed the algorithm in the slides.


2) Region counting

Was able to create a histogram of the pixels. Then found the threshold through finding
the peaks of the histogram and getting the average. Found "T". Algorithm from the slides

Could not get the cell counting to work.
Problems
-   for some reason i get negative values in row 0 when there shouldn't be a pixel before 0



*This assignment was extremely difficult and had a huge initial learning curve*
