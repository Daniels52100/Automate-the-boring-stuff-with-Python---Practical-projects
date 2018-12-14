# This program is executed every 15 minutes when it is programmed to.
# It verifies the email for any mail containing the keyword and then
# executes the command it is told to.

# KEYWORDS:
    # cmd: opens a process given the necessary command line
    # link: opens a given link
    # kw: searches for a keyword command in the commands dictionary

# E-MAIL SYNTAX:
    # Subject: The password is <password>
    # Body: <keyword> <command>\n
    #                .
    #                .
    #                .
    #       <keyword> <command>\n

import imapclient, smtplib, pyzmail, webbrowser, threading, subprocess

def execute(command):
    # Cleaning the command:
    global response
    command = command.strip(' ')
    splitCommand = command.split(' ')
    prefix = splitCommand[0]
    # Commands of opening process:
    if prefix == 'subprocess':
        try:
            subp = subprocess.Popen(command[10:].lstrip(' '))
            response += 'Command: "' + command + '" - executed with success.\n'
        except FileNotFoundError:
            response += 'In command "' + command + '": Couldn\'t find the file.\n'

    # Commands of opening links:
    elif prefix == 'link':
        try:
            link = splitCommand[1]
            webbrowser.open(link)
        except IndexError:
            response += 'In command "' + command + '": There is no link to access.\n'

    # None of the commands above:
    else:
        response += "'" + command + "' doesn't have have a keyword ('subprocess' or 'link')."

# This is where you enter the info about both emails and password.
senderEmail = 'testepythonbiel@gmail.com'
email = 'testepythonbiel@gmail.com'
emailPassword = 'automate2018'
commandPassword = 'lolita'

# Checking for new emails from you with the password:
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(email, emailPassword)
imapObj.select_folder('INBOX')
newIDs = imapObj.search(['UNSEEN', 'FROM', senderEmail, 'SUBJECT', commandPassword])

# Saving all commands in a list:
rawCommandMails = imapObj.fetch(newIDs, ['BODY[]'])
commands = [] 
for id in newIDs:
    commandMail = pyzmail.PyzMessage.factory(rawCommandMails[id][b'BODY[]'])
    if commandMail.text_part != None:
        text = commandMail.text_part.get_payload().decode(commandMail.text_part.charset)
        for line in text.split('\r\n'):
            if line != '': commands.append(line)

# There is no need to delete the emails because they're now seen and won't be considered.
# But if you want to, uncomment next line:
# imapObj.delete_messages(newIDs)    
imapObj.logout()

# Starting a thread for each command received:
response = ''
threadList = []
for cmd in commands:
    threadObj = threading.Thread(target=execute, args=[cmd])
    threadObj.start()
    threadList.append(threadObj)

for thread in threadList:
    thread.join()

# Sending back a response:
if response != '':
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.ehlo()
    smtpObj.login(email, emailPassword)
    # For some reason the body of the email isn't being built correctly.
    smtpObj.sendmail('testepythonbiel@gmail.com', 'testepythonbiel@gmail.com', 'Subject: Last 15 min overview.\n' + response)
    smtpObj.quit()