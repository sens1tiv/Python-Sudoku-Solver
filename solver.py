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

def ReadTable(path):
    fil = open(path, "r")
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

class Chunk:

    chunk = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    filled_o = 9
    filled = 9
    done_numbs = []

    def __init__(self, numbers):
        for i in range(9):
            self.chunk[i] = numbers[i]
            if numbers[i] == 0:
                self.filled -= 1
                self.filled_o -= 1
            else:
                self.done_numbs.append(numbers[i])
                self.done_numbs.sort()

    # Start of the program
table = ReadTable(os.path.join(os.path.dirname(__file__), 'unsolved.csv'))
PrintState(table)

def makeChunkNumber(c_col, c_row):
    temp = []
    for i in range(3):
        for j in range(3):
            temp.append(table[i + (c_col * 3)][j + (c_row * 3)])
    return temp

def makeChunks():
    chunks = [[[], [], []], 
              [[], [], []], 
              [[], [], []]]
    
    for i in range(3):
        for j in range(3):
            chunks[i][j] = Chunk(makeChunkNumber(i, j))
    return chunks

chunks = makeChunks()

possibles = [[[[], [], [], [], [], [], [], [], []], 
              [[], [], [], [], [], [], [], [], []], 
              [[], [], [], [], [], [], [], [], []]],
             [[[], [], [], [], [], [], [], [], []], 
              [[], [], [], [], [], [], [], [], []], 
              [[], [], [], [], [], [], [], [], []]],
             [[[], [], [], [], [], [], [], [], []], 
              [[], [], [], [], [], [], [], [], []], 
              [[], [], [], [], [], [], [], [], []]]]