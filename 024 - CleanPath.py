# This program reduces a path by removing useless subfolders.

import os, shutil, send2trash
# This is where you put the initial folder of the path you want to clean:
path = r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\Teoria\arquivos para teste'
os.chdir(path)

folderCount = 0 # Stores the number of folders that should be deleted.
for folder, subfolders, filenames in os.walk('.'):
    # Verifying if there is only onde folder in the subfolder:
    if len(subfolders) == 1 and len(filenames) == 0:
        folderCount += 1
        continue
    # Moving non-empty folder to the initial path:
    shutil.move(folder, path)
    # Erasing all useless subfolders:
    send2trash.send2trash(folder + '\\..' * (folderCount-1)) # you can replace this by os.rmtree()