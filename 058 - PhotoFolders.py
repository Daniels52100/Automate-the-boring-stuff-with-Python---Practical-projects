import os, shutil
from PIL import Image
# Enter in next line the folder where you want to seek photo folders:
path = 'yourpath'
os.chdir(path)
for folder, subfolders, files in os.walk('.'):
    numOfFiles = len(files)
    numOfPhotos = 0
    for filename in files:
        if filename.endswith('.png') or filename.endswith('.jpg'):
            im = Image.open(filename)
            width, height = im.size
            if width > 500 and height > 500:
                numOfPhotos += 1
    if numOfPhotos > int(numOfFiles / 2):
        shutil.move(folder, folder + ' (Photo Folder)')