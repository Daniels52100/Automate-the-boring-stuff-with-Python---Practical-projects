# This program prints a list of lists as a table. Nested lists must have the same length.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    # Verifying if the given list is a table:
    width = len(table[0])
    isTable = all(map(lambda x: len(x) == width, table[1:]))

    if(isTable):
        # Obtaining the width for each column in table:
        colWidths = []         
        for column in table:
            colWidths.append(max([len(w) for w in column]))

        # Defining lines' and columns' length:
        columns = len(table)
        lines = len(table[0])

        # Printing all elements in table:
        for line in range(lines):
            for column in range(columns):
                print(table[column][line].rjust(colWidths[column]) + ' ', end = '')
            print()
    
    else:
        print('Unable to print: nested lists have different sizes.')

printTable(tableData)
