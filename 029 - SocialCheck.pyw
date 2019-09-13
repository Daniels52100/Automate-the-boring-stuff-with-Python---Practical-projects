#! python3
# This program opens all your social media
# at once, or the ones specified as argument.
import sys, webbrowser
links = {'facebook' : 'https://www.facebook.com/', 'twitter' : 'https://twitter.com/',
         'instagram' : 'https://www.instagram.com/?hl=pt-br'}

if len(sys.argv) == 1:
    # No arguments were given, so we're opening
    # all the links we have.
    [webbrowser.open(link) for link in links.values()]
else:
    # The user specified the links, so we're
    # opening the ones that were given.
    [webbrowser.open(links[key]) for key in sys.argv[1:] if key in links.keys()]
