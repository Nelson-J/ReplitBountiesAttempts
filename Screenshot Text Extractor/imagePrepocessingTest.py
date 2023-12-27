import numpy
import cv2
from matplotlib import pyplot as plt
import os
from PIL import Image
import pytesseract

# Get the directory of the current script
scriptDirectory = os.path.dirname(os.path.abspath(__file__))
os.chdir(scriptDirectory)
cwd = os.getcwd()

OriginalImage = cv2.imread('.\\images\\screenshot_20231014_161426.png')
#Detecting contours
#Read and convert image to grayscale
grayImage = cv2.imread('.\\images\\screenshot_20231014_161426.png',0)
if grayImage is None:
    print("File Does not exist at location: ")
    print(cwd)
    exit(0)

#apply binary threshold
ret, binaryThresh = cv2.threshold(grayImage,167,255,cv2.THRESH_BINARY)
cv2.imwrite('.\\images\\black_white\\grayImage.png',binaryThresh)

#detect contours on binary image using CV2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=binaryThresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

#draw contours on original image
imageCopy = OriginalImage.copy()
cv2.drawContours(image=imageCopy, contours= contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.imwrite('.\\images\\Contouring\\imageContours.png',imageCopy)
