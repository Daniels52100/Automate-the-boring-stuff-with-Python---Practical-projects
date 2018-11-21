#! python3
# This program saves passwords and sends to the clipboard the desired password when executed.
# To execute it from cmd, you must download "14 - NewPasswordLocker.bat" and follow instructions.

import sys, pyperclip, shelve
PASSWORDS = shelve.open(r'C:\Users\Gabriel\Documents\UFU\Cursos e Livros\Livros\Automatize Boring Stuff\Teoria\textos para teste\myPasswords.txt')

if len(sys.argv) < 2:
    print('Usage: python PasswordLocker.py [account] - copy account password')
    sys.exit()

if sys.argv[1] == 'new':
    print('Insert account name (Or nothing to quit):')
    newAccount = input()
    if newAccount == '':
        sys.exit()
    else:
        print('Insert the password. (I won\'t look, I promise!)')
        newPassword = input()
        PASSWORDS[newAccount] = newPassword
        print('Password successfully registered.')
        # Differently from "PasswordLocker.py", in this program we can actually save new 
        # passwords with 'shelve' module, so now this feature is functional.
else:
    account = sys.argv[1] # sys.argv[0] is always a string containing the program's filename.
    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account + '. To register it, execute the program with \'new\' as argument')
PASSWORDS.close()
