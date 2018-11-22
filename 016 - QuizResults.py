# This program simulates 35 tests and corrects them according to answer keys.
# It must be run from the folder where you runned "015 - Random Quiz.py"
from random import randint
from os import chdir
chdir(r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\Teoria\textos para teste\quizzes')

# Creating file that will receive the results:
spreadSheetFile = open('0 - Spreadsheet.txt', 'w')
spreadSheetFile.write('------------------\n')
spreadSheetFile.write('  Student  | Grade\n')
spreadSheetFile.write('-----------+------\n')
for quizNum in range(35):
    studentFile = open('student%s.txt' % (quizNum + 1), 'w')
    keyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'r')
    # Creating the header for the student's test:
    studentFile.write('Name: Student %s\n\nDate: xx/xx/xxxx\n\nPeriod: xx\n\n' % (quizNum+ 1))
    # This way, student answers will start at 7th line.
    rightAnswers = 0
    for questionNum in range(50):
        studentAnswer = 'ABCD'[randint(0,3)]
        studentFile.write('%s. %s\n' % (questionNum + 1, studentAnswer))
    studentFile.close()
    studentFile = open('student%s.txt' % (quizNum + 1), 'r+')
    studentList = studentFile.readlines()
    keyList = keyFile.readlines()
    for textLine in range(50):
        if studentList[textLine + 6] == keyList[textLine]:
            rightAnswers += 1
    studentFile.write('\nStudent %s got %s right answers.' % (quizNum + 1, rightAnswers))
    spreadSheetFile.write(' Student %s'.center(11) % str(quizNum + 1).zfill(2) + '|' + str(rightAnswers).center(6) + '\n')
    studentFile.close()
    keyFile.close()

spreadSheetFile.close()