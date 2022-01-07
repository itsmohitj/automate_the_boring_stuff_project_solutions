# Table Printer

def printTable(arr):
    colWidths = [0] * len(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if len(arr[i][j]) > colWidths[i]:
                colWidths[i] = len(arr[i][j])

    for i in range(len(arr[0])):
        for j in range(len(arr)):
            print(arr[j][i].rjust(colWidths[j]), end=" ")
        print()    

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)