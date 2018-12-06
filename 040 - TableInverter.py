import openpyxl, sys
from os.path import dirname, basename
path = '.\\Practice Projects\\Planilhas para teste\\teste.xlsx'
wb = openpyxl.load_workbook(path)
sheet = wb.active
invWb = openpyxl.Workbook()
invSheet = invWb.active
for i in range(1, sheet.max_row + 1):
    for j in range(1, sheet.max_column + 1):
        invSheet.cell(row=j, column=i).value = sheet.cell(row=i, column=j).value

invWb.save((dirname(path) + '\\inverted_' + basename(path)))
