class Grid:
    def __init__(self, n, m):
        self.adjmat = list()
        self.rows = n  # Number of rows in the grid
        self.column = m  # Number of columns in the grid
        self.vertices = n * m  # Total number of vertices is the number of cells in the grid
        self.vectors = [-1, +1, -n, +n]
        """
            A cell is connected to four neighbouring cells(if they exist) viz :-
                  |
                  |
            ---- cell ----
                  |
                  | 
        """
        for i in range(self.vertices):
            self.adjmat.append(list())
            for j in range(self.vertices):
                self.adjmat[i].append(0)
        self.add_edges()

    def add_edges(self):
        for i in range(self.vertices):
            for j in self.vectors:
                if (i + 1) % self.rows == 0 and j == 1:  # Last cell of a some row cannot be connected to first cell
                    # of next row
                    continue
                if j == -1 and i % self.rows == 0:  # First cell of some row cannot be connected to the last cell of
                    # previous row
                    continue
                if self.is_valid(i + j):
                    self.adjmat[i][i + j] = 1

    def is_valid(self, n):
        if 0 <= n <= self.vertices - 1:  # cells are numbered from 0 to (product of rows and columns)-1
            return True
        return False


g = Grid(2, 3)
"""
    0 -- 1
    |    |
    |    |
    2 -- 3
    |    |
    |    |
    4 -- 5
"""
print(g.adjmat)
