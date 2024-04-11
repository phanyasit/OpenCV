import cv2

img = cv2.imread("image/cat.jpg")
print(img.shape)

cv2.imshow('image',img)
k = cv2.waitKey(0)

#accesses pixel at x=100, y=20
(b,g,r) = img[20,100]
#accesses pixel at x=25, y=75
(b,g,r) = img[75,25]
#accesses pixel at x=100, y=20
(b,g,r) = img[90,85]