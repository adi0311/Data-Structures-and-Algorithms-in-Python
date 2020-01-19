import numpy
from collections import deque


class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjMatrix = numpy.zeros((vertices, vertices))
        self._size = 0

    def add_edge(self, u, v, w=1):
        self._adjMatrix[u][v] = w

    def delete_edge(self, u, v):
        self._adjMatrix[u][v] = 0

    def bfs(self, source):
        i = source
        q = deque()
        q.append(source)
        l = [0] * self._vertices
        l[i] = 1
        print(i, end='->')
        while q:
            i = q.popleft()
            for j in range(self._vertices):
                if self._adjMatrix[i][j] == 1 and l[j] == 0:
                    print(j, end='->')
                    q.append(j)
                    l[j] = 1


g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 5)
g.add_edge(0, 4)
g.add_edge(0, 2)
g.add_edge(2, 5)
g.add_edge(2, 3)
g.add_edge(6, 3)
g.add_edge(1, 3)
g.add_edge(6, 4)
g.add_edge(1, 6)
g.bfs(0)
