#! python3
# This program saves passwords and sends to the clipboard the desired password when executed.
# To open it, we type "5 - PasswordLocker" <argument> on cmd prompt.
# "5 - PasswordLocker.bat" must be downloaded along with PasswordLocker.py so that the command above works. 

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python PasswordLocker.py [account] - copy account password')
    sys.exit()

if sys.argv[1] == 'new':
    print('Insert account name (Or nothing to quit):')
    newAccount = input()
    print('Insert the password. (I won\'t look, I promise!)')
    newPassword = input()
    PASSWORDS[newAccount] = newPassword
    print('Password successfully registered.')
    # Because we didn't use actual files in this program, the new password won't be saved.
    # We would need a file containing the PASSWORDS dictionary to save it, and open the file in the program.
    # The objective with this feature is to test the argv's logic.
else:
    account = sys.argv[1] # sys.argv[0] is always a string containing the program's filename.
    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account + '. To register it, execute the program with \'new\' as argument')
