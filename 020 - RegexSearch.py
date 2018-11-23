# This program searches in .txt files in a folder for a user-supplied regex.

import re, os
# Reading folder and regex:
print('Enter the absolute path to the folder:')
path = input()
os.chdir(path)
print('\nEnter the regular expression:')
regex = input()
regex = re.escape(regex) # Escapes all special characters.
regex = re.compile(regex)
print()

# Searching for .txt files in folder:
fileList = os.listdir('.')
for files in fileList:
    if files.endswith('.txt'):
        print('Matches found in ' + files + ':\n')
        text = open(files, 'r').readlines()
        # Searching for regex in file:
        for line in text:
            if regex.search(line) != None:
                # Printing line where the regex is:
                print(' line %s' % (text.index(line) + 1) + ': ' + line)
            print()
        