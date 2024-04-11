import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import cv2
import easyocr
import pandas as pd

image = cv2.imread(r'D:\python-opencv-main\image\thai-sign.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_wb = cv2.threshold(image_gray, 110, 255, cv2.THRESH_BINARY)[1]
ROI_ = image_wb[35:72,106:216]
reader = easyocr.Reader(['th','en'],gpu=True)
result = reader.readtext(ROI_, detail=0)
print(result)

# cv2.imshow('image',image)
# cv2.imshow('image_gray',image_gray)
# cv2.imshow('image_wb',image_wb[28:48,30:268])
# cv2.waitkey(0)
# cv2.destroyAllWindows