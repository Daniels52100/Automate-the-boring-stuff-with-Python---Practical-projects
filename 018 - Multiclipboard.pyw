#! python3
# This program saves and loads pieces of text to clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve, pyperclip, sys
from os import chdir
chdir(r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\Teoria\textos para teste\mcb')
mcbShelf = shelve.open('mcb')
# Saving clipboard content:
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save': 
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelf:
            mcbShelf.pop(sys.argv[2])

elif len(sys.argv) == 2:
    # Listing keywords and loading content:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        for keys in list(mcbShelf.keys()):
            del mcbShelf[keys]