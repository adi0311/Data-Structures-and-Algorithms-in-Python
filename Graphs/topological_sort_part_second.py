"""
    DocTests
    >>> G = Graph(6)
    >>> G.insert(0, 1)
    >>> G.insert(0, 2)
    >>> G.insert(0, 4)
    >>> G.insert(0, 5)
    >>> G.insert(1, 2)
    >>> G.insert(1, 4)
    >>> G.insert(2, 3)
    >>> G.insert(3, 5)
    >>> G.insert(4, 5)
    >>> G.topological_sort()
    [0, 1, 4, 2, 3, 5]
"""

"""
    Note -> Topological Sort only works on DAG(Directed Acyclic Graphs).
    Graphs with cycles can never have a topological order of nodes.
"""
from collections import defaultdict as dd   # To remove key errors.


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
        # Node is put in ordering list in the function itself.
        self.vis[node] = True
        for m in self.adjmat[node].keys():
            if not self.vis[m]:
                i = self.dfs(i, m)
        self.ordering[i] = node
        return i-1

    def topological_sort(self):
        # This function is optimised as compared to Part One with respect to both space and time.
        i = self.vertices-1
        for node in range(self.vertices):
            if not self.vis[node]:
                i = self.dfs(i, node)
        return self.ordering
