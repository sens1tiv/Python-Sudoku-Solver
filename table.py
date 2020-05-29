
class Table:
    def __init__(self, numbers):
        self.numbers = numbers
        self.rows = []
        self.columns = []
        self.chunks = [[], [], []]
        self.filled = 0
        self.filled_o = 0
        
        self.initRows()
        self.initColumns()
        self.initChunks()
        
        
    def initRows(self):
        for i in range(9):
            self.rows.append(self.Row(i, self.numbers))
            self.filled += self.rows[i].filled
            self.filled_o += self.rows[i].filled_o
            
    def initColumns(self):
        for i in range(9):
            self.columns.append(self.Column(i, self.numbers))
            
    def initChunks(self):
        for i in range(3):
            for j in range(3):
                self.chunks[i].append(self.Chunk(i, j, self.numbers))
                
    def update(self, row, column, number):
        self.numbers[row][column] = number
        self.rows[row].numbers[column] = number
        self.columns[column].numbers[row] = number
        self.chunks[row // 3][column // 3].numbers[(row // 3) * (column // 3)] = number
        self.filled += 1
    
        # Classes
    class Row:
        def __init__(self, row, numbers):
            self.numbers = []
            self.filled = 9
            self.filled_o = 9
            
            for i in range(9):
                self.numbers.append(numbers[row][i])
                
                if self.numbers[i] == 0:
                    self.filled_o -= 1
                    self.filled -= 1
    
    class Column:
        def __init__(self, column, numbers):
            self.numbers = []
            self.filled = 9
            self.filled_o = 9
            
            for i in range(9):
                self.numbers.append(numbers[i][column])
                
                if self.numbers[i] == 0:
                    self.filled_o -= 1
                    self.filled -= 1
        
    class Chunk:
        def __init__(self, row, column, numbers):
            self.numbers = []
            self.filled = 9
            self.filled_o = 9
            
            temp = [-1]
            for i in range(3):
                for j in range(3):
                    temp.append(numbers[i + (row * 3)][j + (column * 3)])
            temp.remove(-1)
            for i in range(9):
                self.numbers.append(temp[i])
                if self.numbers[i] == 0:
                    self.filled -= 1
                    self.filled_o -= 1