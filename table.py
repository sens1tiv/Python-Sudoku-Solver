
class Table:
    
    numbers = [[], [], [], 
               [], [], [], 
               [], [], []
               ]
    filled_o = 81
    filled = 81
    
    """done_numbs = [[[], [], []], 
                  [[], [], []], 
                  [[], [], []]]"""
    
    rows = []
    columns = []
    chunks = [[0, 0, 0], 
              [0, 0, 0], 
              [0, 0, 0]]
    
    def __init__(self, numbers):
        for i in range(9):
            for j in range(9):
                    self.numbers = numbers
        self.initRows()
        self.initColumns()
        self.initChunks()
        
        for i in range(9):
            print(self.rows[i].numbers)
        print(len(self.rows))
    
    def initRows(self):
        for i in range(9):
            self.rows.append(self.Row(i, self.numbers))
        for i in range(9):
            self.rows[i] = self.Row(i, self.numbers)
            
    def initColumns(self):
        for i in range(9):
            self.columns.append(self.Column(i, self.numbers))
            
    def initChunks(self):
        for i in range(3):
            for j in range(3):
                self.chunks[i].append(self.Chunk(i, j, self.numbers))
    
    class Row:
        
        numbers  = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        filled_o = 9
        filled   = 9
        """done     = [0, 0, 0, 0, 0, 0, 0, 0, 0]"""
        
        def __init__(self, row, numbers):
            for i in range(9):
                self.numbers[i] = numbers[row][i]
                if self.numbers[i] == 0:
                    self.filled_o -= 1
                    self.filled -= 1
                """else:
                    self.done[i] = self.numbers[i]"""
            
    
    class Column:
        
        numbers  = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        filled_o = 9
        filled   = 9
        """done     = [0, 0, 0, 0, 0, 0, 0, 0, 0]"""
        
        def __init__(self, column, numbers):
            for i in range(9):
                self.numbers[i] = numbers[i][column]
                
                if self.numbers[i] == 0:
                    self.filled_o -= 1
                    self.filled -= 1
                """else:
                    self.done.append(self.numbers[i])
                    self.done.sort()"""
        
    class Chunk:
        
        numbers  = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        filled_o = 9
        filled   = 9
        """done     = [0, 0, 0, 0, 0, 0, 0, 0, 0]"""
        
        def __init__(self, row, column, numbers):
            temp = [-1]
            for i in range(3):
                for j in range(3):
                    temp.append(numbers[i + (row * 3)][j + (column * 3)])
            temp.remove(-1)
            for i in range(9):
                self.numbers[i] = temp[i]
                if self.numbers[i] == 0:
                    self.filled -= 1
                    self.filled_o -= 1
                """else:
                    self.done.append(self.numbers[i])
                    self.done.sort()"""