
class generate_board():
    def __init__(self, n_bombs, n_rows, n_cols):
        self.columns = []
        self.n_bombs = n_bombs
        self.row_count = n_rows
        self.col_count = n_cols
        self.cell = self.cell
        has_bomb = [True, False]
    class cell:
        def __init__(self, bomb, val):
            self.bomb = bomb
            self.value = val
    def get_surounding_bombs(self, row,col):
        count = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if (row,col) != (row+i,col+j):
                    if self.columns[row+i][col+j].value == -1:
                        count += 1
        return count
    def start_gen(self):
        for i in range(0,self.row_count):
            rows=[]
            for x in range(self.col_count):
                temp_cell = self.cell(False,0)
                rows.append(temp_cell)
            self.columns.append(rows)
        
        for i in range(0,self.n_bombs):
            row = random.randint(1,self.row_count-2)
            col = random.randint(1,self.col_count-2)
            self.columns[row][col].bomb = True
            self.columns[row][col].value = -1
            
        for row_count in range(1,self.row_count-1):
            for col_count in range(1,self.col_count-1):
                if self.columns[row_count][col_count].bomb != True:
                    self.columns[row_count][col_count].value = self.get_surounding_bombs(row_count,col_count)
        self.columns = [x[1:-1] for x in self.columns[1:-1]]
        for row in self.columns:
            print([x.value for x in row])
