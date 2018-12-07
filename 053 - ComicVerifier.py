import re, os, bs4, requests, sys, datetime
from requests.exceptions import ConnectionError, HTTPError
from shutil import move
# Comic image file regex:
comicRegex = re.compile(r'''
    ^(\d*)          # Index part
    (\(unread\))?   # Unread marker
    (\.jpg)$        # Extension
''', re.VERBOSE)

# Trying to create the folder with the comics and finding the most recent in it:
AbsPathToComic = r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\Practice Projects\exocomics'
os.makedirs(AbsPathToComic, exist_ok=True)
os.chdir(AbsPathToComic)
    # Creating a text file to warn if any errors occur:
open('0000 - error warning.txt', 'a').close()
while True:
    # Retrieving most recent comic's index:
    if os.listdir('.') != []:
        lastComicDownloaded = os.listdir('.')[-1]
        lastIndex = int(comicRegex.search(lastComicDownloaded).group(1))
    else:
        lastIndex = 0
    try:
        # Trying to access site in next non-downloaded comic's page:
        pageUrl = 'https://www.exocomics.com/%s' % (str(lastIndex + 1))
        res = requests.get(pageUrl)
        res.raise_for_status()
    except (ConnectionError, TimeoutError):
        errorLog = open('0000 - error warning.txt', 'a')
        errorLog.write('\n' + str(datetime.datetime.now()) + ' - Error while downloading page ' + pageUrl)
        errorLog.close()
        move('0000 - error warning.txt', '0000 - error warning (NEW ERROR).txt')
        sys.exit()
    except HTTPError:
        sys.exit()

    # Downloading image and marking as unread:
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    try:
        # Finding image URL:
        comicElem = soup.select('.image-style-main-comic')
        comicUrl = comicElem[0].get('src')
        # Downloading and saving image:
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFilename = os.path.basename(comicUrl)
            # Adding unread marker to file:
        imageFilename = imageFilename[:-4].zfill(4) + '(unread)' + imageFilename[-4:]
        imageFile = open(imageFilename, 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    except (ConnectionError, HTTPError, IndexError, TimeoutError):
        errorLog = open('0000 - error warning.txt', 'a')
        errorLog.write('\n' + str(datetime.datetime.now()) + ' - Error while downloading image ' + comicUrl + '.')
        errorLog.close()
        move('0000 - error warning.txt', '0000 - error warning (NEW ERROR).txt')
        sys.exit()