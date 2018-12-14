import pyautogui, time, os
from PIL import Image
friendsList = {'Renatin', 'Ronquifuca', 'Uarlinston', 'Temer'}
pyautogui.PAUSE = 1.0
searchButtonIm = 'searchbutton.png'
chatBoxIm = 'chatbox.png'
message = 'Teste'
os.chdir(r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\Practice Projects')

print('5 seconds to start sending messages.')
time.sleep(5)

for friend in friendsList:
    try:
        # Searching for friend:
        for i in range(3):
            searchBtn = pyautogui.locateOnScreen(searchButtonIm)
            time.sleep(1)
        searchBtnCenter = pyautogui.center(searchBtn)
        pyautogui.click(searchBtnCenter)
        pyautogui.typewrite(friend)
        pyautogui.typewrite(['enter'])

        # Typing message:
        pyautogui.typewrite(message)
        pyautogui.typewrite(['enter'])

    except TypeError:
        print('Couldnt find one of the fields. Try setting Whatsapp Web to fullscreen.')
    
