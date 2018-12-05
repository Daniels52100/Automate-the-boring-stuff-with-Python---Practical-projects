# This program reads a text formatted as a table and converts it to a spreadsheet.
import pyperclip, openpyxl

# Reading the table from clipboard:
tableTxt = pyperclip.paste()

# Creating rows:
tableTxt = tableTxt.split('\r\n')
for i in range(len(tableTxt)):
    # Splitting elements and eliminating empty strings
    # resulted from multiple spaces:
    aux = tableTxt[i].split(' ')
    tableTxt[i] = []
    for element in aux:
        if element != '':
            tableTxt[i].append(element)

# Creating sheet:
wb = openpyxl.Workbook()
tableXl = wb.active
for row in range(1, len(tableTxt) + 1): # Rows and columns start with 1
    for col in range(1, len(tableTxt[row-1]) + 1):
        # List elements' indexes start with 0.
        tableXl.cell(row=row, column=col).value = tableTxt[row-1][col-1]

wb.save('.\\Practice Projects\\Planilhas para teste\\TableFromText.xlsx')      