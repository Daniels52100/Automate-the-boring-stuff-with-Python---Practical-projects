# This program adds the folder's name as prefix to all the files in it.
import os
from shutil import move
# Changing the CWD to the folder that should be changed.
os.chdir(r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\Teoria\arquivos para teste\teste')
prefix = os.path.basename(os.getcwd()) + '_'
for filename in os.listdir('.'):
    move(filename, prefix + filename)