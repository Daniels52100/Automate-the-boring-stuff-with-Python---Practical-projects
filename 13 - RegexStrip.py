# This program is meant to be implemented in others as auxiliar function. 
# It works the same way as strip().
import re
def regStrip(*args):
    text = str(args[0])
    try:
        stripped = str(args[1])
        regex = re.compile(r'^' + stripped + r'+|' + stripped + r'+$')
    except IndexError:
        regex = re.compile(r'^\s+|\s+$')
       
    return regex.sub('',args[0])


