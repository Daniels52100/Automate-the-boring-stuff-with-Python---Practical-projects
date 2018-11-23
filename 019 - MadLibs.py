# This program searchers for the words ADJECTIVE, NOUN, ADVERB and VERB and substitutes them for user input.

from os import chdir
import re
chdir(r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\Teoria\textos para teste\madlibs')

# Regular expressions:
adjectiveRegex = re.compile('ADJECTIVE')
nounRegex = re.compile('NOUN')
adverbRegex = re.compile('ADVERB')
verbRegex = re.compile('VERB')

# Grouping regexes into a dictionary:
regexDict = {'adjective' : adjectiveRegex, 'noun' : nounRegex, 'adverb' : adverbRegex, 'verb' : verbRegex}

# Opening files:
print('Insert a text file in madlibs folder (without extension):')
filename = input()
text = open(filename + '.txt','r')
newText = open('new' + filename + '.txt','w')
textlines = text.readlines()

# Searching for each regex in each word:
for line in textlines:
    for word in line.split(' '):
        for key in regexDict.keys():
            if regexDict[key].search(word) != None:
                # Asking user for substitute word:
                print('Insert ' + key + ':')
                sub = input()
                # Replacing the word found:
                word = regexDict[key].sub(sub,word)
                # We can't just attribute input to word variable because that would omit punctuation within the word.
                break
        if word[-1] != '\n': word += ' '
        # Adding spaces to words at the end of the lines would cause indentation on next line.
        newText.write(word)
newText.close()
text.close()

