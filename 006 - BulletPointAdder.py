#! python3
# This program adds bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()
lineList = text.split('\n')
for i in range(len(lineList)):
    lineList[i] = '* ' + lineList[i]
text = '\n'.join(lineList)
pyperclip.copy(text)
