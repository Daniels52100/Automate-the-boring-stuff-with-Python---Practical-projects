# This program searches a folder for all files in it with a specific extension
#  and copies all of them to a new folder.

import os, shutil
# This is where you put the file in which you want to search de extension:
path = r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\Teoria\arquivos para teste'
path = os.path.abspath(path)
os.chdir(path)
cwd = os.getcwd()

# This is where you put the extension you want to search for:
extension = '.txt'

# Creating the folder:
newFolder = extension[1:] + '_files'
if not os.path.exists('.\\' + newFolder):
    os.makedirs(newFolder)

# Searching for files with the specified extension:
for folder, subfolders, filenames in os.walk('.'):
    if folder == newFolder:
        continue
    for filename in filenames:
            if filename.endswith(extension) and filename not in os.listdir(newFolder):
                shutil.copy(os.path.join(folder,filename), newFolder)