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

    # Start of the program
my_table = Table(ReadTable(os.path.join(os.path.dirname(__file__), 'unsolved.csv')))
PrintState(my_table.numbers)
#print(my_table.rows[4].numbers)
for i in range(9):
    print(my_table.rows[i].numbers)

"""possibles = [[[[], [], [], [], [], [], [], [], []], 
              [[], [], [], [], [], [], [], [], []], 
              [[], [], [], [], [], [], [], [], []]],
             [[[], [], [], [], [], [], [], [], []], 
              [[], [], [], [], [], [], [], [], []], 
              [[], [], [], [], [], [], [], [], []]],
             [[[], [], [], [], [], [], [], [], []], 
              [[], [], [], [], [], [], [], [], []], 
              [[], [], [], [], [], [], [], [], []]]]"""