# This program converts a list to a string.

l = ['apples', 'bananas', 'tofu', 'cats']

def displayList(list):
    i = 0
    while True:
        print(l[i], end = '')
        if i == len(l) - 1:
            print('.')
            break
        if i < len(l) - 2:
            print(', ', end = '')
        if i == len(l) - 2:
            print(' and ', end = '')
        i+=1

displayList(l)
