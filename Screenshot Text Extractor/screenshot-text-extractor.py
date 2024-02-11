from imagePrepocessingTest import preprocessFromFile
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
#bwTestImage = r'.\\images\\to_OCR\\ready.png'

fullNames=[]
companyNames=[]
roles=[]
attendeeData=[]

matchCompany=None
matchName=None
matchRole=None

#testerVariables
countNames=0
countCompanies=0
countRoles=0

#for every file in the folder
for filename  in os.listdir(image_folder):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        imageFromFile = cv2.imread(os.path.join(image_folder,filename))
        readyImage = preprocessFromFile(imageFromFile)
        extractedText = pytesseract.image_to_string(readyImage)
        print(extractedText)

        #prepocessing text
        lines = extractedText.split("\n")

        for line in lines:
            #getting full names
            patternName = r"^(\b[A-Z][a-z]*\b\s\b[A-Z][a-z]*\b)$" #match consecutive words starting with a capital letter
            matchName = re.findall(patternName,line)
            #print(matchName)
            #company
            patternCompany = r'^([A-Z].*?)\s-\s' #get text before first hyphen
            matchCompany = re.findall(patternCompany, line) 

            #roles
            patternRoles = r'(?<=-)(?:(?!\b\w\b).)*' #match text after the first hyphen, ignore one-character words
            matchRole = re.findall(patternRoles,line)
                
            #add data to list only if Name, Role and Company are set.
            if (not matchName) or (not matchRole) or (not matchCompany):
                continue
            else:
                fullNames.append(matchName[0])
                countNames+=1
                companyNames.append(matchCompany[0])
                countCompanies+=1
                roles.append(matchRole[0])
                countRoles+=1

                print(matchName[0])
                #print(matchRole[0])
                #print(matchCompany[0])
                #print("======================")
        

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