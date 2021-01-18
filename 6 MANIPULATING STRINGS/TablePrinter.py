# Chapter 6
# Project: Table Printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(data):
    for column in range(len(data[0])):
        for row in range(len(data)):
            colWidths = len(max(data[row], key=len))
            print(str(data[row][column]).rjust(colWidths),end=" ")
        print('\n')


printTable(tableData)

# return:  
#   apples Alice  dogs

#  oranges   Bob  cats 

# cherries Carol moose 

#   banana David goose 
