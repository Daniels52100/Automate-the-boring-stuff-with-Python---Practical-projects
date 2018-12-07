import os, shutil, sys

# Reading arguments:
if len(sys.argv) == 2:
    readComics = sys.argv[1]
else:
    print('Pass the index of the most recent comic you read.')
    sys.exit()

# Following path must be your comics folder's path:
AbsPathToComic = r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\Practice Projects\exocomics'
os.chdir(AbsPathToComic)

# Excluding error warning from list:
for comic in os.listdir('.')[1:]:
    # Obtaining comic's index:
    comicIndex = int(comic[0:4].lstrip('0'))
    if comicIndex < readComics and comic[4:12] == '(unread)':
        # Renaming:
        shutil.move(comic, comic[0:4] + comic[12:])