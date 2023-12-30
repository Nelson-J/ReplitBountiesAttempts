import numpy as np
import cv2
import os

def preprocessFromFile(file):
    # Get the directory of the current script
    scriptDirectory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(scriptDirectory)
    cwd = os.getcwd()

    #OriginalImage = cv2.imread('.\\images\\screenshot_20231014_161427.png')
    OriginalImage = cv2.imread(file)

    #Read and convert image to grayscale
    grayImage = cv2.imread(file,0)
    if (grayImage is None) or (OriginalImage is None):
        print("File Does not exist at location: ")
        print(cwd)
        exit(0)

    #apply binary threshold
    ret, binaryThresh = cv2.threshold(grayImage, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    #cv2.imwrite('.\\images\\black_white\\grayImage.png',binaryThresh)

    #detect contours on binary image using CV2.CHAIN_APPROX_SIMPLE
    contours, hierarchy = cv2.findContours(image=binaryThresh, mode=cv2.RETR_EXTERNAL, method= cv2.CHAIN_APPROX_SIMPLE)

    # Filter OUT the contours that are letters
    filtered_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 240:
            filtered_contours.append(contour)

    # Draw the filtered contours on the original image i.e. Now: the original image includes contours
    cv2.drawContours(OriginalImage, filtered_contours, -1, (0, 255, 0), 2)

    #Removing the contours from the original image
    #initialize mask with same size as original image and with white pixels (225)
    mask = np.ones(OriginalImage.shape[:2], dtype='uint8')*225

    #draw contours on the mask image; draw all the contours(-1), with black (0), fill the contours (-1)
    cv2.drawContours(mask,contours,-1, 0, -1)
    #maintain only areas within the contours
    readyImage = cv2.bitwise_and(OriginalImage,OriginalImage,mask=mask)

   # cv2.imwrite('.\\images\\to_OCR\\ready.png',readyImage)

    return readyImage