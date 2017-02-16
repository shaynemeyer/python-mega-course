import cv2

im_g = cv2.imread('smallgray.png', 0)

first = im_g[2,4]

print(first)

for i in im_g.flat:
    print(i)