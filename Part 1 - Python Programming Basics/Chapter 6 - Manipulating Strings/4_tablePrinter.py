# ! python3

tableData = [['apples', 'oranges', 'cherris', 'banana'], # 0
             ['Alice', 'Bob', 'Carol', 'David'],         # 1
             ['dogs', 'cats', 'moose', 'goose']]         # 2

def printTable(table):
    columnWidths = [0] * len(table)
    
    # find the maximum string length for every sublist
    for i in range(len(table)):
        for value in table[i]:
            if len(value) > columnWidths[i]:
                columnWidths[i] = len(value)
    
    print(columnWidths)
    print()

    # print the list of data
    for i in range(len(table[0])): # 0 - 3
        for j in range(len(table)): # 0 - 2
            print(str(table[j][i]).rjust(columnWidths[j]) + '   ', end = '')
        print()

printTable(tableData)