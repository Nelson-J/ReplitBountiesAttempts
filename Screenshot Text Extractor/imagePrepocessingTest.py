import numpy
import cv2
from matplotlib import pyplot
import os
from PIL import Image
import pytesseract

#enforce current working directory
scriptDirectory = os.path.dirname(os.path.abspath(__file__ ))
os.chdir(scriptDirectory)

#print(os.getcwd())

imageFolder= r'.\images'
image2 = cv2.imread('.\images\test.png')
for filename in os.listdir(imageFolder):
    image = cv2.imread(os.path.join(imageFolder,filename))
    #image = cv2.imread(imageObject)
    readyImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
   # ret, readyImage = cv2.threshold(readyImage,0,255,cv2.THRESH_BINARY,cv2.THRESH_OTSU)
    readyImage = cv2.adaptiveThreshold(readyImage,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,5)
    #ret, readyImage = cv2.threshold(readyImage, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    recognizedText = pytesseract.image_to_string(readyImage)

#print(recognizedText)
#image2.save('.\images\test.png', dpi=(300,300))
pyplot.subplot(121), pyplot.imshow(image)
pyplot.subplot(122), pyplot.imshow(readyImage)
pyplot.show()
