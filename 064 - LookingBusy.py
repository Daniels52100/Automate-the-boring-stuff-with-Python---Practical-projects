import pyautogui, time
print('Press Ctrl-C to exit.')
while True:
    try:
        for i in range(10):
            time.sleep(1)
        pyautogui.moveRel(5,0)
        for i in range(10):
            time.sleep(1)
        pyautogui.moveRel(-5, 0)
    except KeyboardInterrupt:
        break