# This program prints a list of lists as a table. Nested lists must have the same length.

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    # Verifying if the given list is a table:
    isTable = True
    for l1 in  range(len(table)):
        for l2 in range(l1+1, len(table)):
            # Comparing a list's length to all the ones that come after it in the table.
            if len(table[l1]) != len(table[l2]):
                isTable = False

    if(isTable):
        # Obtaining the width for each column in table:
        colWidth = []         
        for i in range(len(table)):
            colWidth.append(0)
            for element in table[i]:
                if len(element) > colWidth[i]:
                    colWidth[i] = len(element)

        # Defining lines' and columns' length:
        colLength = len(table)
        lineLength = len(table[0])

        # Printing all elements in table:
        for line in range(lineLength):
            for column in range(colLength):
                print(table[column][line].rjust(colWidth[column]) + ' ', end = '')
            print()
    
    else:
        print('Unable to print: nested lists have different sizes.')

printTable(tableData)