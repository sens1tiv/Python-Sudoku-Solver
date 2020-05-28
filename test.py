
class Table:

    rows = []

    def __init__(self):
        self.initRows()

    def initRows(self):
        for i in range(9):
            self.rows.append(self.Row(i*10))
            print(self.rows[i].n)

    class Row:
        n = 0
        def __init__(self, n):
            self.n = n

my_table = Table()
"""for i in range(9):
    print(my_table.rows[i].n)"""