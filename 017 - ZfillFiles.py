# I had to fill my files' indexes in "Practice Projects" folders with zeros so they would be in order, so i made this:
# To apply it to any folder, just change the path in 4th line to the path to your folder.
import os, re
os.chdir(r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\Practice Projects')
indexRegex = re.compile(r'^(\d+)')
for files in os.listdir('.'):
    newIndex = indexRegex.search(files).group(1).zfill(3) # Adding 0's to the index.
    newFile = indexRegex.sub(newIndex, files) # Replacing the index.
    os.rename(files, newFile) # Replacing the name.
