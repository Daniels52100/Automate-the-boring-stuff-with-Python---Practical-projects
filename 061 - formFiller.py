# formFiller.py - Automatically fills in the form.
import pyautogui, time
nameField = (535, 245)
submitButton = (515, 715)
submitButtonColor = (66, 133, 244)
submitAnotherLink = (865, 360)
formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
             'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
             'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
             'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
             'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}]

pyautogui.PAUSE = 1.0
for person in formData:
    # Give the user a chance to kill the script.
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    # Wait until the form page has loaded
    while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        time.sleep(0.5)
    
    print('Entering %s info...' % (person['name']))
    pyautogui.click(nameField[0], nameField[1])

    # Fill out the name field.
    pyautogui.typewrite(person['name'] + '\t')

    # Fill out the greatest fear(s) field.
    pyautogui.typewrite(person['fear'] + '\t')

    # Fill out the source of wizard powers field.
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])
    if person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t'])
    if person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    if person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])
    
    # Fill out the robocop field.
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    if person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    if person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    if person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right',  '\t'])
    if person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right',  '\t'])

    # Fill out the additional comments field.
    pyautogui.typewrite(person['comments'] + '\t')
    # Click submit.
    pyautogui.press('enter')
    # Wait until form page has loaded.
    print('Clicked submit.')
    time.sleep(5)
    # Click the submit another response link
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])