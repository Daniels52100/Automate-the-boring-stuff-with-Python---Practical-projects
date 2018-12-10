import random, smtplib, datetime, os
emails = {'John' : 'testepythonbiel@gmail.com', 'Gabriel' : 'testepythonbiel@gmail.com', 'Joseph' : 'testepythonbiel@gmail.com', 'Anna' : 'testepythonbiel@gmail.com'}
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']
os.makedirs('.\\Practice Projects\\Chores', exist_ok=True)
os.chdir('.\\Practice Projects\\Chores')

# Logging into email:
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()
password = input()
smtpObj.login('testepythonbiel@gmail.com', password)

# Creating weekly text file:
date = datetime.datetime.now().strftime('%b %d')
choresTxt = open('Chores for %s.txt' % (date), 'w+')

# Sending emails:
for name, mail in emails.items():
    chore = random.choice(chores)
    smtpObj.sendmail('testepythonbiel@gmail.com', mail, 'Subject: Chore of the week.\nDear %s, your chore for \
    this week is %s.' % (name, chore))
    chores.remove(chore)
    choresTxt.write('%s will do %s.\n' % (name, chore))

smtpObj.quit()