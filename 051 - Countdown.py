
import time, subprocess, os
os.chdir(r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\automate_online-materials')
timeLeft = 5
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft -= 1
# At the end of the countdown, play a sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)