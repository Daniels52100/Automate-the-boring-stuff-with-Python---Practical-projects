#! python3

# This program finds URLs in clipboard text and sends a list of them back to the clipboard.

import re, pyperclip
text = str(pyperclip.paste())
UrlRegex = re.compile(r'''(
    (^https?://)        # protocol
    (\S+)               # name
    (\.[a-z]{2,})       # dot-something
    (/\S*)*             # sub-pages
)''',re.VERBOSE)

UrlList = []
for groups in UrlRegex.findall(text):
    UrlList.append(str(groups[0])) # groups[0] represents the entire expression, so we're appending the whole link to UrlList.
if len(UrlList) > 0:
    pyperclip.copy('\n'.join(UrlList))
    print('Found ' + str(len(UrlList)) + ' URLs.')
    print('\n'.join(UrlList))
    print('List copied to clipboard.')
else:
    print('No URLs were found.')

