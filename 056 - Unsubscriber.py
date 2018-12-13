import imapclient, datetime, bs4, pyzmail, re, webbrowser, sys
imapclient._MAXLINE = 10000000

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
# Finding unsubscribe button in each email:
for i in range(1, len(rawMsgs) + 1):
    # skipping deleted e-mails:
    if rawMsgs[i] != {}:
        message = pyzmail.PyzMessage.factory(rawMsgs[i][b'BODY[]'])
        if message.html_part != None:
                html = message.html_part.get_payload().decode(message.html_part.charset)
                # Parsing
                soup = bs4.BeautifulSoup(html, features="lxml")
                for tag in soup.find_all():
                # Looking for the word 'unsubscribe' in each tag:
                        if regex.search(tag.getText()) != None:
                                # opening links with the word 'unsubscribe' in text:
                                webbrowser.open(tag.get('href'))
imapObj.logout()