"""
    Reach the exit in minimum number of steps.
    Print the shortest path.
    '#' represents the rocks.
    '.' represents the safe path.
    'S' is the entrance of the Dungeon.
    'E' is the exit of the Dungeon.
"""

from collections import deque


def is_valid(x, y):
    if x < 0 or y < 0 or x >= n or y >= m or vis[x][y] or dungeon[x][y] == '#':
        #Return False if cell is visited or has rocks or is not valid.
        return False
    return True


def neighbours(a, b):
    global cellsNext
    for i in range(4):
        xDash, yDash = a+xvector[i], b+yvector[i]
        if is_valid(xDash, yDash):
            vis[xDash][yDash] = True
            x.append(xDash)
            y.append(yDash)
            cellsNext += 1


def find_parents(): #Implementing BFS to get the parent of each cell
    parent = [[None for i in range(m)] for j in range(n)]
    visited = [[False for i in range(m)] for j in range(n)]
    qx, qy = deque(), deque()
    qx.append(startx)
    qy.append(starty)
    visited[startx][starty] = True
    while len(qx) != 0:
        a, b = qx.popleft(), qy.popleft()
        for i in range(4):
            aDash, bDash = a+xvector[i], b+yvector[i]
            if 0 <= aDash < n and 0 <= bDash < m:
                if not(visited[aDash][bDash]) and dungeon[aDash][bDash] != '#':
                    parent[aDash][bDash] = (a, b)
                    qx.append(aDash)
                    qy.append(bDash)
                    visited[aDash][bDash] = True
    return parent


def get_the_path():
    nowx, nowy = endx, endy
    parents = find_parents()
    path = []
    while parents[nowx][nowy] is not None:
        path.append((nowx, nowy))
        nowx, nowy = parents[nowx][nowy]
    path.append((startx, starty))
    return path


def get_out_of_dungeon():
    global won, cellsLeft, cellsNext, numberOfMoves
    x.append(startx)
    y.append(starty)
    vis[startx][starty] = True
    while len(x) > 0:
        a, b = x.popleft(), y.popleft()
        if dungeon[a][b] == 'E':
            won = True
            break
        neighbours(a, b)
        cellsLeft -= 1
        if cellsLeft == 0:
            cellsLeft = cellsNext
            cellsNext = 0
            numberOfMoves += 1
    if won:
        return numberOfMoves
    return "EXIT NOT REACHED"


xvector = [1, -1, 0, 0]
yvector = [0, 0, 1, -1]
n, m = 4, 4 #4 rows and 4 columns
dungeon = [
    ['S', '#', 'E', '#'],
    ['.', '#', '.', '.'],
    ['.', '.', '.', '#'],
    ['#', '#', '.', '#']
]
"""
    Dungeon looks like this.
    S(0, 0) #(0, 1) E(0, 2) .(0, 3)
    .(1, 0) #(1, 1) .(1, 2) .(1, 3)
    .(2, 0) .(2, 1) .(2, 2) #(2, 3)
    #(3, 0) #(3, 1) .(3, 2) #(3, 3)
"""
startx, starty = 0, 0   #The starting point of the Dungeon
endx, endy = 0, 2   #The exit of the Dungeon
x, y = deque(), deque() #To keep track of the shortest path
numberOfMoves, cellsNext, cellsLeft = 0, 0, 1   #To keep count of the shortest path
vis = [[False for i in range(m)] for j in range(n)] #To keep track if a cell is visited or not
won = False

print(get_out_of_dungeon())
if won:
    print("SHORTEST PATH")
    path = reversed(get_the_path())
    print(*path)