from PIL import Image
import pytesseract
import os
import re
import csv

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

currentDirectory = os.getcwd()

# Get the directory of the current script
scriptDirectory = os.path.dirname(os.path.abspath(__file__))

# Set the current working directory
os.chdir(scriptDirectory)

image_folder = r'.\images'

for filename in os.listdir(image_folder):
    image = Image.open(os.path.join(image_folder, filename))
    extractedText = pytesseract.image_to_string(image)

fullNames=[]
companyNames=[]
roles=[]
attendeeData=[]

#prepocessing text
lines = extractedText.split("\n")


for line in lines:
       
    #getting full names
    if len(line)>2 and line[0].islower() and any(char.isupper for char in line):
    #line starts with a small letter, contains a capital letter, and has a length greater than 2

        patternName = r'\b([A-Z][a-zA-Z]*\s+\b[A-Z][a-zA-Z]*)' #match consecutive words starting with a capital letter
        matchName = re.findall(patternName,line)
        
        if matchName:
            fullNames.append(matchName[0])

    if not fullNames: #take only picture that has three required information
        continue

    #company
    patternCompany = r'^([A-Z].*?)\s-\s' #get text before first hyphen
    matchCompany = re.findall(patternCompany, line) 
    if matchCompany: #no company without fullName
        companyNames.append(matchCompany[0])

    #roles
    patternRoles = r'(?<=-)(?:(?!\b\w\b).)*' #match text after the first hyphen, ignore one-character words
    matchRole = re.findall(patternRoles,line)
    if matchRole: 
        roles.append(matchRole[0])

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
    writer.writerows(attendeeData)