import cv2
import numpy as np

# Load the image
img = cv2.imread("C:\\Users\\ANELKA\\ReplitBounties\\Screenshot Text Extractor\\image.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# Find the external contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter out the contours that are letters
filtered_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 240:
        filtered_contours.append(contour)

# Draw the filtered contours on the original image
cv2.drawContours(img, filtered_contours, -1, (0, 255, 0), 2)

# Display the result
cv2.imwrite('Result.png', img)

#Remove the filered contours on the original image
mask = np.ones(img.shape[:2], dtype='uint8')*225

cv2.drawContours(mask,contours,-1, 0, -1)

img = cv2.bitwise_and(img,img,mask=mask)

cv2.imwrite('Final.png',img=img)