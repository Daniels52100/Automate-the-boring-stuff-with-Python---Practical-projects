#! python3
# This program opens google maps using a given address from
# command line or clipboard.
# You can run it from cmd with "028 - MapIt.bat" <address>

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https:\\www.google.com/maps/place/' + address)