# This program finds gaps in file indexes and corrects them.
# e.g. spam001.txt and then spam003.txt.
import shutil, os, re

def removeGaps():
    for i in range(1, len(fileList)): # i starts in 1 so we can take 0 as previous element.
        # The index part of the file is the second element in each element of fileList
        # because it is the second group in the regex.
        currFileIndex = int(fileList[i][1])
        prevFileIndex = int(fileList[i-1][1])
        if currFileIndex > prevFileIndex + 1:
            filename = ''.join(fileList[i])
            currFileIndex = prevFileIndex + 1
            fileList[i][1] = str(currFileIndex)
            newName = ''.join(fileList[i])
            shutil.move(filename, newName)

def createGap():
    gapStart = len(fileList)
    # Making sure the gap starts in the index interval:
    while gapStart > len(fileList) - 1 or gapStart < 0:
        print('After what index should the gap start?')
        gapStart = int(input())
    print('What is the size of the gap?')
    gapSize = int(input())
    # Renaming files from the last one to the first after gapStart:
    for i in range(len(fileList) - 1, gapStart - 1, -1):
        filename = ''.join(fileList[i])
        fileIndex = int(fileList[i][1])
        fileIndex += gapSize
        fileList[i][1] = str(fileIndex)
        newName = ''.join(fileList[i])
        shutil.move(filename, newName)

# Creating the regular expresison:
print('Enter the prefix:')
prefix = input()
indexRegex = re.compile('(' + prefix + ')' + # Given prefix
        r'''(\d+)                            # Index
            (.*)?$                           # Text after index
        ''',re.VERBOSE)
        # I didn't include extension in the regex so that
        # it can be useful for folders as well.
        
# Searching the folder for indexed files:
print('Enter the path:')
path = input()
os.chdir(path)

# Obtaining the list of files with the given prefix:
fileList = []
for filename in os.listdir(path):
    mo = indexRegex.search(filename)
    if mo == None:
        continue
    splitFilename = list(mo.groups())
    fileList.append(splitFilename)

# Verifying if there are gaps:
gapsExist = False
for fileIndex in range(1, len(fileList)):
    currFileIndex = int(fileList[fileIndex][1])
    prevFileIndex = int(fileList[fileIndex - 1][1])
    if currFileIndex > prevFileIndex + 1:
        gapsExist = True
        break
 
if gapsExist:
    print('Gaps were found. Do you wish to remove them? (yes or anything else for no)')
    option = input()
    if option == 'yes':
        removeGaps()
        print('Done.')

else:
    print('No gaps were found. Do you wish to create any? (yes or anything else for no)')
    option = input()
    if option == 'yes':
        createGap()
        print('Done.')