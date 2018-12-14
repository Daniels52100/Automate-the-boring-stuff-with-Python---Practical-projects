#! python3
import webbrowser, os, pyautogui, sys, time
# This program does part of the procedure of uploading a file to github.
# it logs into your account, goes to upload section and load the give file.
# [Usage] upToGit.bat <password> "<path to the file>"

# Changing the directory to 'uptogit pics' folder.
os.chdir(r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\Practice Projects\uptogit pics')

# Getting filename:
if len(sys.argv) != 3:
    print('[Usage] upToGit.bat <password> "<path to the file>"')
    sys.exit()
pathToFile = sys.argv[2]

USERNAME = 'gabrielmsollero'
PASSWORD = sys.argv[1]
REPOSITORY = 'Automate-the-boring-stuff-with-python---Practical-Projects'
# You can also inform the repository via argv after the filename. For that, uncomment next line:
# REPOSITORY = sys.argv[3]
MAXIMIZE_BUTTON = 'maximizebutton.png'
MINIMIZE_BUTTON = 'minimizebutton.png'
SIGN_IN_BUTTON = 'signin.png'
EMAIL_TEXT_BOX = 'emailtxtbox.png'
LOADED_PAGE_IMAGE = 'loadedpage.png'
UPLOAD_FILES_BUTTON = 'uploadfilesbutton.png'
CHOOSE_FILES_BUTTON = 'chooseyourfiles.png'
COMMIT_CHANGES_BUTTON = 'commitchanges.png'

def Find(image):
    """
    Enters a loop and leaves it only when it finds the given image.
    Returns the coordinates of the image's center.
    """
    startTime = time.time()
    while True:
        endTime = time.time()
        if endTime > startTime + 10:
            print('Couldn\'t find image: %s' % image)
            sys.exit()
        coordinates = pyautogui.locateOnScreen(image)
        if coordinates != None:
            return pyautogui.center(coordinates)


# opening and maximizing GitHub:
webbrowser.open('https://github.com')
while True:
    maxBtn = pyautogui.locateOnScreen(MAXIMIZE_BUTTON)
    minBtn = pyautogui.locateOnScreen(MINIMIZE_BUTTON)
    if maxBtn != None:
        Xmax, Ymax = maxBtn[0:2]
        pyautogui.click((Xmax + 117, Ymax + 13))
        break
    if minBtn != None:
        # already on fullscreen
        break

# Signing in:
pyautogui.scroll(1000)
pyautogui.click(Find(SIGN_IN_BUTTON))
Find(EMAIL_TEXT_BOX)
pyautogui.typewrite(USERNAME + '\t' + PASSWORD)
pyautogui.typewrite(['enter'])

# Redirecting to uploading section:
    # The current page is closed, and then a new one is opened straight in uploads section.
Find(LOADED_PAGE_IMAGE)
pyautogui.hotkey('ctrl', 'w')
webbrowser.open('https://github.com/' + USERNAME + '/' + REPOSITORY + '/upload/master')

# Uploading:
pyautogui.click(Find(CHOOSE_FILES_BUTTON))
pyautogui.typewrite(pathToFile)
pyautogui.typewrite(['enter'])