# This program converts all phone numbers in a sheet to the same format.
# Part of the code was recycled from "008 - PhoneAndEmailFinder.py"

import re, openpyxl

# Regular Expression for phone numbers:
phoneRegex = re.compile(r'''(
    (0?[1-9]{2}|\(0?[1-9]{2}\)) # DDD: 'xx', '0xx', '(xx)' ou '(0xx)'
    (\s*|-|\s-\s)?              # separator (' ', '-' ou ' - ')
    (9?\d{4})                   # first four digits (9 is optional) ('9xxxx')
    (\s*|-|\s-\s)?              # separator (' ', '-' ou ' - ')
    (\d{4})                     # last four digits ('xxxx')
)''', re.VERBOSE)

# Opening workbook:
wb = openpyxl.load_workbook('.\\Practice Projects\\Planilhas para teste\\Telefones.xlsx')
sheet = wb.active

# Searching for the regex in each cell:
for row in sheet.iter_rows():
    for cell in row:
        # This is the recycled part from PhoneAndEmailFinder.py:
        for groups in phoneRegex.findall(str(cell.value)):
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
            cell.value = phoneNum

wb.save('.\\Practice Projects\\Planilhas para teste\\Telefones.xlsx')

