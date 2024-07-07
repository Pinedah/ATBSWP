# ! python3

tableData = [['apples', 'oranges', 'cherris', 'banana'], # 0
             ['Alice', 'Bob', 'Carol', 'David'],         # 1
             ['dogs', 'cats', 'moose', 'goose']]         # 2

def printTable(table):
    columnWidths = [0] * len(table)
    for i in range(len(table)):
        for value in table[i]:
            if len(value) > columnWidths[i]:
                columnWidths[i] = len(value)
    print(columnWidths)
    print()
    for i in range(len(table[0])):
        print(str(table[0][i]).rjust(columnWidths[0]), str(table[1][i]).rjust(columnWidths[1]), str(table[2][i]).rjust(columnWidths[2]), sep = "     ")

printTable(tableData)