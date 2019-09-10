# This program converts a list to a string.

l = ['apples', 'bananas', 'tofu', 'cats']

def displayList(list):
    print((', ').join(l[:-1]) + 'and ' + l[-1])

displayList(l)
