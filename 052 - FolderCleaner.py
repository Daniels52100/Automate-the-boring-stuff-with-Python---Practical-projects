# This program cleans a folder and gives the user 3 seconds to cancel de deletion of each file.
import os, time, sys
from shutil import rmtree
if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    print('Usage: insert a path to a folder you want to clean as argument.')
    sys.exit()

try:
    os.chdir(path)
except FileNotFoundError:
    print('Unable to reach the folder. Try entering it between quotes.')
    sys.exit()
print('Deleting all files in ' + os.path.basename(path) + '...')
print('For each file, you\'ll have 3 seconds to cancel the deletion. Press Ctrl + C if you want to cancel')
for filename in os.listdir('.'):
    try:
        print('\nDeleting %s in ' % (filename), end='')
        for i in range (3, 0, -1):
            print(str(i) + '... ', end = '')
            time.sleep(1)
        if os.path.isdir(filename):
            rmtree(filename)
        else:
            os.unlink(filename)
        print('Deleted.')
    except KeyboardInterrupt:
        print('\nDeletion cancelled.')
