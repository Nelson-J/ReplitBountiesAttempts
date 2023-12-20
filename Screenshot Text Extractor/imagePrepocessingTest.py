import numpy
import cv2
from matplotlib import pyplot
import os
from PIL import Image

#enforce current working directory
#scriptDirectory = os.path.dirname(os.path.abspath(__file__ ))
#os.chdir(scriptDirectory)

print(os.getcwd())

imageFolder= r'.\images'

for filename in os.listdir(imageFolder):
    imageObject = Image.open(os.path.join(imageFolder,filename))
    image = cv2.imread(imageObject)
    readyImage = cv2.fastNlMeansDenoisingColored(image,None, 10, 10, 7, 15)

pyplot.subplot(121), pyplot.imshow(image)
pyplot.subplot(122), pyplot.imshow(readyImage)
pyplot.show()
