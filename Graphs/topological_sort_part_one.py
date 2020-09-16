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
from collections import defaultdict as dd


class Graph():
    def __init__(self, vertices):
        self.adjmat = dd(dict)
        self.vertices = vertices
        self.vis = [False for i in range(self.vertices)]  # To check the visited status of each node while TopSort.
        for i in range(vertices):
            self.adjmat[i] = dd(int)

    def insert(self, u, v, w=1):
        self.adjmat[u][v] = w

    def dfs(self, node, result):
        self.vis[node] = True  # Mark current node as visited
        for m in self.adjmat[node].keys():
            if not self.vis[m]:
                self.dfs(m, result)  # Calling dfs for all reachable nodes
        result.append(node)  # Appending the nodes in the visited list(i.e. result)
        return result

    def topological_sort(self):
        i = self.vertices - 1
        ordering = [0 for i in range(self.vertices)]
        for at in range(self.vertices):
            if not self.vis[at]:
                visited = self.dfs(at, [])
                for j in visited:
                    # Adding the visited node from end of ordering array
                    ordering[i] = j
                    i -= 1
        return ordering
