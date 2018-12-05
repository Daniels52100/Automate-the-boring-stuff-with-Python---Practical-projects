#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL) # Comment this to debug.

print('Googling...') # display text while downloading the Google page
res = requests.get('https://www.google.com.br/search?q=' + ' '.join(sys.argv[1:]))
logging.debug('Searching: https://www.google.com.br/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features="html.parser")
logging.debug('bs4 object created.')
# Open a browser tab for each result.
linkElems = soup.select('h3.r a')
logging.debug('Links found: ' + str(len(linkElems)))
if len(linkElems) == 0:
    logging.error('No results found.')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    logging.debug('Opening: ' + 'http://google.com' + linkElems[i].get('href'))