# This program finds gaps in file indexes and corrects them.
# e.g. spam001.txt and then spam003.txt.
import shutil, os, re

def removeGaps(files):
    for i in range(1, len(files)): # i starts in 1 so we can take 0 as previous element.
        # The index part of the file is the second element in each element of fileList
        # because it is the second group in the regex.
        currFileIndex = int(files[i][1])
        prevFileIndex = int(files[i-1][1])
        if currFileIndex != prevFileIndex + 1:
            filename = ''.join(files[i])
            currFileIndex = prevFileIndex + 1
            files[i][1] = str(currFileIndex)
            newName = ''.join(files[i])
            shutil.move(filename, newName)

#    for i in filter(lambda j: indexes[j] != indexes[j-1] + 1, range(1, len(files))):

def createGap(files):
    gapStart = len(files)
    # Making sure the gap starts in the index interval:
    while gapStart > len(files) - 1 or gapStart < 0:
        print('After what index should the gap start?')
        gapStart = int(input())
    print('What is the size of the gap?')
    gapSize = int(input())
    # Renaming files from the last one to the first after gapStart:
    for i in range(len(files) - 1, gapStart - 1, -1):
        filename = ''.join(files[i])
        fileIndex = int(files[i][1])
        fileIndex += gapSize
        files[i][1] = str(fileIndex)
        newName = ''.join(files[i])
        shutil.move(filename, newName)

def isSequence(lst): # verifies if a list is sequential, e.g. [1, 2, 3] and not [1, 2, 4].
    return all([lst[i] == lst[i-1] + 1 for i in range(1, len(lst))])

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

mos = [indexRegex.search(f) for f in os.listdir(path)]
fileList = [list(mo.groups()) for mo in mos if mo]
indexes = [int(l[1]) for l in fileList]

if not isSequence(indexes):
    print('Gaps were found. Do you wish to remove them? (yes or anything else for no)')
    option = input()
    if option == 'yes':
        removeGaps(fileList)
        print('Done.')

else:
    print('No gaps were found. Do you wish to create any? (yes or anything else for no)')
    option = input()
    if option == 'yes':
        createGap(fileList)
        print('Done.')
