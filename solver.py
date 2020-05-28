# Built-In libraries
from os import system, name
import os.path

# Downloaded libraries


# Custom libraries
import tts


        # Functions
def Cls():
    if name == 'nt': 
        _ = system('cls')

Cls()

fn = os.path.join(os.path.dirname(__file__), 'unsolved.csv')
fil = open(fn, "r")
sud = []

for i in range(9):
    row = fil.readline()
    row = row[:len(row)-1]
    splitted = row.split(';')

    temp = []
    for j in range(9):
        temp.append(int(splitted[j]))
    sud.append(temp)

fil.close()

for i in range(9):
    msg = ""
    for j in range(9):
        if sud[i][j] != 0:
            msg += str(sud[i][j])
            msg += " "
        else:
            msg += "  "
    print(msg)