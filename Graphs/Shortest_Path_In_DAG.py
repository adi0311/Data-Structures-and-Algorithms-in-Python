"""
    Doctests
    >>> G = Graph(6)
    >>> G.insert(0, 1, 3)
    >>> G.insert(0, 5, 5)
    >>> G.insert(1, 5, -9)
    >>> G.insert(1, 3, 6)
    >>> G.insert(5, 3, -8)
    >>> G.insert(3, 2, 5)
    >>> G.insert(3, 4, 7)
    >>> G.insert(2, 4, 4)
    >>> G.shortest_path(0)
    defaultdict(<class 'int'>, {0: 0, 1: 3, 5: -6, 3: -14, 2: -9, 4: -7})
    >>> G.longest_path(0)
    defaultdict(<class 'int'>, {0: 0, 1: 3, 5: 5, 3: 9, 2: 14, 4: 18})
"""
"""
    It is a SSSP(Single Source Shortest Path) Algorithm.
    It is useful in finding shortest and longest path in DAGs
    (Directed Acyclic Graphs).
    Dijkstra Algorithm fails in case of negative weight of edges
    but this algorithm really shines at this area.
"""
from collections import defaultdict as dd


class Graph:
    def __init__(self, vertices):
        self.adjmat = dd(dict)
        self.vertices = vertices
        self.ordering = [0 for i in range(self.vertices)]
        self.vis = [False for i in range(self.vertices)]
        for i in range(vertices):
            self.adjmat[i] = dd(int)

    def insert(self, u, v, w=1):
        self.adjmat[u][v] = w

    def dfs(self, i, node):
        self.vis[node] = True
        for m in self.adjmat[node].keys():
            if not self.vis[m]:
                i = self.dfs(i, m)
        self.ordering[i] = node
        return i-1

    def topological_sort(self):
        i = self.vertices-1
        for node in range(self.vertices):
            if not self.vis[node]:
                i = self.dfs(i, node)
        return self.ordering

    def shortest_path(self, start):
        order = self.topological_sort()
        dist = dd(int)
        dist[start] = 0
        for i in range(self.vertices):
            node = order[i]
            if node in dist.keys():
                for j in range(self.vertices):
                    if j in self.adjmat[node].keys():
                        mindist = dist[node]+self.adjmat[node][j]
                        if j not in dist.keys():
                            dist[j] = mindist
                        else:
                            dist[j] = min(dist[j], mindist)
        return dist

    # Multiply each edge weight by -1 and find the shortest path.
    # Longest path is the -1*shortest path.
    def longest_path(self, start):
        mat = dd(dict)
        for i in self.adjmat.keys():
            for j in self.adjmat[i].keys():
                mat[i][j] = -self.adjmat[i][j]
        order = self.topological_sort()
        dist = dd(int)
        dist[start] = 0
        for i in range(self.vertices):
            node = order[i]
            if node in dist.keys():
                for j in range(self.vertices):
                    if j in mat[node].keys():
                        mindist = dist[node]+mat[node][j]
                        if j not in dist.keys():
                            dist[j] = mindist
                        else:
                            dist[j] = min(dist[j], mindist)
        for i in range(len(dist)):
            dist[i] *= -1
        return dist
