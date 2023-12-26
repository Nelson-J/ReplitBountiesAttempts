from PIL import Image
import pytesseract
import os
import re
import csv
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

currentDirectory = os.getcwd()

# Get the directory of the current script
scriptDirectory = os.path.dirname(os.path.abspath(__file__))

# Set the current working directory
os.chdir(scriptDirectory)

image_folder = r'.\images'

fullNames=[]
companyNames=[]
roles=[]
attendeeData=[]

#testerVariables
countNames=0
countCompanies=0
countRoles=0

#for every file in the folder
for filename in os.listdir(image_folder):
    #image = Image.open(os.path.join(image_folder, filename))
    imageFromFile = cv2.imread(os.path.join(image_folder,filename))
    #preprocessing image
    grayscaleImage = cv2.cvtColor(imageFromFile,cv2.COLOR_BGR2GRAY)
    imageThreshold = cv2.adaptiveThreshold(grayscaleImage,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,5)
    #ret, imageThreshold = cv2.threshold(grayscaleImage, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    extractedText = pytesseract.image_to_string(imageThreshold)
    #print(extractedText)

    #prepocessing text
    lines = extractedText.split("\n")

    for line in lines:
        
        #getting full names
        if len(line)>2 and line[0].islower() and any(char.isupper for char in line):
        #line starts with a small letter, contains a capital letter, and has a length greater than 2

            patternName = r'\b([A-Z][a-zA-Z]*\s+\b[A-Z][a-zA-Z]*)' #match consecutive words starting with a capital letter
            matchName = re.findall(patternName,line)
            
            if matchName:
                print(matchName[0])
                fullNames.append(matchName[0])
                countNames+=1

        if not fullNames: #take only picture that has three required information
            continue

        #company
        patternCompany = r'^([A-Z].*?)\s-\s' #get text before first hyphen
        matchCompany = re.findall(patternCompany, line) 
        if matchCompany: #no company without fullName
            #print(matchCompany[0])
            companyNames.append(matchCompany[0])
            countCompanies+=1

        #roles
        patternRoles = r'(?<=-)(?:(?!\b\w\b).)*' #match text after the first hyphen, ignore one-character words
        matchRole = re.findall(patternRoles,line)
        if matchRole: 
            #print(matchRole[0])
            roles.append(matchRole[0])
            countRoles+=1

print('Name Count ', countNames)
print('Company Count ',countCompanies)
print('Role Count ',countRoles)
''' 
#storing extracted data in memory
for count in range(0, len(fullNames)):
    attendeeData.append({
    'Full Name':fullNames[count],
    'Company Name':companyNames[count],
    'Role':roles[count]
    })

#write extracted data to csv file
with open('attendeeData.csv','w',newline='') as csvFile:
    fieldNames = ['Full Name', 'Company Name', 'Role']
    writer = csv.DictWriter(csvFile, fieldnames=fieldNames)

    writer.writeheader
    writer.writerows(attendeeData) '''