#! python3
# This program tests the strength of a password.
# You must download "12 - PwStrength.bat" and type "12 - PwStrength.bat" <password> on cmd to run it.

import sys
if len(sys.argv) < 2:
    print('You must enter a password as argument to be tested.')
    sys.exit()
password = sys.argv[1]
strong = True
if not (len(password) >= 8 and password.isalnum() and not password.isupper() and not password.islower()):
    strong = False
if(strong):
    print('The password is strong.')
else:
    print('The password isn\'t strong')
