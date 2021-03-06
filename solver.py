# Built-In libraries
from os import system, name
import os.path

# Downloaded libraries


# Custom libraries
import tts
from table import Table


        # Functions
def Cls():
    if name == 'nt': 
        _ = system('cls')
Cls()

def ReadTable(path):
    fil = open(path, "r")
    sud = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]
          ]

    for i in range(9):
        row = fil.readline()
        row = row[:len(row)-1]
        splitted = row.split(';')

        temp = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for j in range(9):
            temp[j] = int(splitted[j])
        sud[i] = temp
    
    fil.close()
    return sud

def PrintState(table):
    for i in range(9):
        msg = ""
        for j in range(9):
            if table[i][j] != 0:
                msg += str(table[i][j])
            else:
                msg += "."
            
            if j  == 2 or j == 5:
                msg += "|"
        print(msg)

        if i == 2 or i == 5:
            print("===========")

    print("")
    print("Done: " + str(my_table.filled) + "/81\n")

possibles = [[[], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], []], 
             [[], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], []]
            ]
possibles_c = possibles
    
def Solve():
    for i in range(9):
        checkRow(i)

def checkRow(row):
    for i in range(9):
        if my_table.rows[row].numbers[i] == 0:
            for j in range(1, 10):
                if j not in my_table.rows[row].numbers:
                    checkColumn(row, i, j)
            
def checkColumn(row, column, number):
    if number not in my_table.columns[column].numbers:
        checkChunk(row, column, number)
            
def checkChunk(row, column, number):
    chunkIndX = row // 3
    chunkIndY = column // 3
    global possibles
    if number not in my_table.chunks[chunkIndX][chunkIndY].numbers:
        possibles[row][column].append(number)

def fillLonelys():
    global possibles
    
    #posses()
    rowses()
    
    wasLonely = False
    
    for i in range(9):
        for j in range(9):
            poss = possibles[i][j]
            if len(poss) == 1:
                my_table.update(i, j, poss[0])
                removePossibles(i, j, poss[0])
                
                if not wasLonely:
                    wasLonely = True

    #print("")
    return wasLonely

def rowses():

    for i in range(3):
        msg_row = ""
        for j in range(9):
            msg_cell = ""
            for k in range(3):
                if len(possibles[i][j]) >= 1:
                    pass

    
    for i in range(3):
        msg_row = ""
        for j in range(9):
            msg_cell = ""
            for k in range(len(possibles[i][j])):
                for l in range(3):
                    if possibles[i][j][k] == l:
                        msg_cell += str(l)
                    else:
                        msg_cell += "."
            
            if j == 2 or j == 6:
                msg_cell += "|"

            msg_row += msg_cell + " "

        print(msg_row)
                
def tryRandom():
    global possibles
    global possibles_c
    global my_table
    global my_table_c
    my_table_c = my_table
    possibles_c = possibles
    #print("try random")
    
    for i in range(9):
        for j in range(9):
            poss = possibles[i][j]
            if len(poss) == 2:
                my_table.update(i, j, poss[0])
                removePossibles(i, j, poss[0])
                i = 9
                j = 9
                break
             
def removePossibles(x, y, n):
    global possibles
    possibles[x][y].remove(n)
    for j in range(0, 9):
        for k in range(len(possibles[x][j])):
            if possibles[x][j][k] == n:
                del possibles[x][j][k]
                break
    for i in range(0, 9):
        for k in range(len(possibles[i][y])):
            if possibles[i][y][k] == n:
                del possibles[i][y][k]
                break

    temp = []
    cX = (x // 3) * 3
    cY = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if len(possibles[cX+i][cY+j]) >= 1:
                temp.append(possibles[cX+i][cY+j])
            for k in range(len(possibles[cX+i][cY+j])):
                if possibles[cX+i][cY+j][k] == n:
                    del possibles[cX+i][cY+j][k]
                    break

    #print(str(x+1) + "-" + str(y+1) + ": " + str(n) + str(temp))
    
def posses():
    global possibles
    for i in range(0, 9):
        for j in range(0, 9):
            if len(possibles[i][j]) > 0:
                print(str(i+1) + "-" + str(j+1) + ": " + str(possibles[i][j]))
    print("")

    # Start of the program
my_table = Table(ReadTable(os.path.join(os.path.dirname(__file__), 'unsolved2.csv')))
my_table_c = my_table

Solve()
PrintState(my_table.numbers)
for i in range(10):
    if not fillLonelys():
        pass
        #tryRandom()
        break
    PrintState(my_table.numbers)
    
for i in range(10):
    if not fillLonelys() and my_table.filled < 81:
        print("is no gud")
        break
    PrintState(my_table.numbers)
    posses()