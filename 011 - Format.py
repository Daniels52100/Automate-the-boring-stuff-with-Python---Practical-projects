#! python3
# This program removes multiple spaces, repeated words and punctuation from clipboard text.
import re, pyperclip
text = pyperclip.paste()

repSpacesRegex = re.compile(r'(\s){2,}') # Two or more occurrences of spaces.

repWordsRegex = re.compile(r'\b(\w+)(\s\1\b)+',re.IGNORECASE) # A word followed by a space and then the same word.

repPuncRegex = re.compile(r'(\.|\?|!|,){2,}') # Two or more occurrences of punctuation.

newText = repSpacesRegex.sub(r'\1', text) 
newText = repWordsRegex.sub(r'\1', newText) # Replacing reps by the last occurrence.
newText = repPuncRegex.sub(r'\1', newText)

if text == newText:
    print('No changings were made.')
else:
    pyperclip.copy(newText)
    print('Formatted text sent to clipboard.')
