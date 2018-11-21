
#! python3
# This program finds all  brazillian phone numbers and email addresses in the clipboard text.
# You must download "8 - PhoneAndEmailFinder.bat" to execute it from cmd.

import pyperclip, re

# Regular Expression for phone numbers:
phoneRegex = re.compile(r'''(
    (0?[1-9]{2}|\(0?[1-9]{2}\)) # DDD: 'xx', '0xx', '(xx)' ou '(0xx)'
    (\s*|-|\s-\s)?              # separator (' ', '-' ou ' - ')
    (9?\d{4})                   # first four digits (9 is optional) ('9xxxx')
    (\s*|-|\s-\s)?              # separator (' ', '-' ou ' - ')
    (\d{4})                     # last four digits ('xxxx')
)''', re.VERBOSE)

#Regular Expression for e-mails:
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4}){1,2}  # dot-something
)''', re.VERBOSE)

text = str(pyperclip.paste())
phoneMatches = []
emailMatches = []
for groups in phoneRegex.findall(text):
    # Phone numbers standardization:
    # Standardazing DDD:
    ddd = str(groups[1])
    if '(' in ddd:
        ddd = ddd[1:-1]
        # Removing first and last character from ddd (parenthesis).
    if '0' in ddd:
        ddd = ddd[1:]
        # Removing first character from ddd. ('0')
    phoneNum = '(' + ddd + ') ' + groups[3] + ' ' + groups[5]
    phoneMatches.append(phoneNum)

for groups in emailRegex.findall(text):
    emailMatches.append(groups[0]) # groups[0] stores the whole RE.

# Copying results to clipboard:
matches = phoneMatches + emailMatches
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Found ' + str(len(phoneMatches)) + ' phone number(s) and ' + str(len(emailMatches)) + ' e-mail address(es):')
    print('\n'.join(matches))
    print('List copied to clipboard.')
else:
    print('No phone numbers or email addresses found.')
