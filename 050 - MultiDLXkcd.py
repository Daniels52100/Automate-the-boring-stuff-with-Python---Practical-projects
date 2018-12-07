# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.
import requests, os, bs4, threading
os.makedirs('.\\automate_online-materials\\xkcd', exist_ok=True)
os.chdir('.\\automate_online-materials\\xkcd')

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
        try:
            print('Downloading page https://xkcd.com/%s...' % (urlNumber))
            res = requests.get('https://xkcd.com/%s' % (urlNumber))
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, features="lxml")

            # Find the URL of the comic image.
            comicElem = soup.select('#comic img')
            if comicElem == []:
                print('Could not find comic image.')
            else:
                comicUrl = comicElem[0].get('src')
                # Download the image.
                print('Downloading image %s...' % (comicUrl))
                res = requests.get('http:' + comicUrl)
                res.raise_for_status()

                # Save the image
                    # Without the index, we don't know the order of the images.
                imageFile = open(str(urlNumber) + '-' + os.path.basename(comicUrl), 'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close() 
        except requests.exceptions.HTTPError:
            # Skipping not found pages:
            print('Something went wrong. Couldn\'t download https://xkcd.com/%s...' % (urlNumber))
            continue
# Create and start the Thread objects.
downloadThreads = []
for i in range(0, 1400, 100):
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')