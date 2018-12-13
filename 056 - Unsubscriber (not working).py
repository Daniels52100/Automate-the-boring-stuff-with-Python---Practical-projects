import imapclient, datetime, bs4, pyzmail, re, webbrowser, sys, threading
imapclient._MAXLINE = 10000000

def searchUnsub(end, start):
        for i in range(start, end - 1, -1):
        # skipping deleted e-mails:
                if rawMsgs[uids[i]] != {}:
                        message = pyzmail.PyzMessage.factory(rawMsgs[uids[i]][b'BODY[]'])
                        if message.html_part != None:
                                html = message.html_part.get_payload().decode(message.html_part.charset)
                                # Parsing
                                soup = bs4.BeautifulSoup(html, features="lxml")
                                for tag in soup.find_all():
                                # Looking for the word 'unsubscribe' in each tag:
                                        if regex.search(tag.getText()) != None:
                                                # opening links with the word 'unsubscribe' in text:
                                                webbrowser.open(tag.get('href'))
# Verifying arguments:
if len(sys.argv != 2):
        print('[Usage]: py.exe Unsubscriber.py <email> <password>')
        sys.exit()
# Unsub regex:
regex = re.compile(r'(.*)?unsub(scribe)?(.*)?', re.DOTALL | re.IGNORECASE)

# Logging in:
email = sys.argv[1]
password = sys.argv[2]
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
try:
        imapObj.login(email, password)
except imapclient.exceptions.LoginError:
        print('Login error. Wrong email or password.')
        sys.exit()

# Finding emails since 30 days ago:
imapObj.select_folder('INBOX', readonly=True)
monthAgo = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%d-%b-%Y')
uids = imapObj.search(['SINCE', monthAgo])
rawMsgs = imapObj.fetch(uids, ['BODY[]'])
# Creating a thread for every 20 emails or less:
threadStart = len(uids)
threadEnd = threadStart - 20
threadList = []
while threadEnd != -1:
        # Preventing index errors:
        if threadEnd >= 19:
                threadEnd = threadStart - 20
                threadStart -= 20        
        else:
                threadEnd = -1
        threadObj = threading.Thread(target=searchUnsub, args=[threadStart, threadEnd])
        threadObj.start()
        threadList.append(threadObj)
                
for thread in threadList:
        thread.join()

imapObj.logout()
