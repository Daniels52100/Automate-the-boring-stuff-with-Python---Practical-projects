# This program prints on screen the largest files in a given folder
# and deletes the ones the user wants to.
import os, send2trash

# Enter the path you want to search here:
path = r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\Teoria\arquivos para teste'
# Enter the maximum size here (in bytes):
maxSize = 0

bigFilesList = []
for folder, subfolders, filenames in os.walk(path):
    for filename in filenames:
        # Getting actual file's name and size:
        filename = os.path.join(folder,filename)
        fileSize = os.path.getsize(filename)
        if fileSize > maxSize:
            filename = os.path.abspath(filename)
            # Adding file to a list and printing it:
            bigFilesList.append(filename)
            print(str(len(bigFilesList)) + ' - ' + filename + '- Size: ' + str(fileSize) + ' bytes.')

print('Do you want to delete any of them? (yes or anything else for no)')
answer = input()
if answer == 'yes':
    print('Enter the indexes of the files you want to delete (or enter nothing to stop):')
    while True:
        fileIndex = input()
        if fileIndex == '':
            break
        print('Deleting ' + bigFilesList[int(fileIndex) - 1] + '...')
        send2trash.send2trash(bigFilesList[int(fileIndex)-1])
        # You can replace the command above by os.rmlink(bigFilesList[int(fileIndex)-1]) to effectively delete the file.
        print('Done.')
        
