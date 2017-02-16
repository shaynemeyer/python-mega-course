import cv2
import numpy

im_g = cv2.imread('smallgray.png', 0)

first = im_g[2,4]

# print(first)

for i in im_g.flat:
    print(i)

ims = numpy.hstack((im_g, im_g))

print(ims)