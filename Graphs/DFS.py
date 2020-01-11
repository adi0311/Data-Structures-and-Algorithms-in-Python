import numpy


class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjMatrix = numpy.zeros((vertices, vertices))
        self._visited = [False] * vertices

    def add_edge(self, u, v, w=1):
        self._adjMatrix[u][v] = w

    def delete_edge(self, u, v):
        self._adjMatrix[u][v] = 0

    def dfs(self, source):
        if not self._visited[source]:
            print(source, end='->')
            self._visited[source] = True
            for j in range(self._vertices):
                if self._adjMatrix[source][j] == 1 and not self._visited[j]:
                    self.dfs(j)


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
g.dfs(0)
