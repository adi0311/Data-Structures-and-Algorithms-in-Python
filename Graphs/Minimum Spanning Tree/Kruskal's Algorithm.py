from collections import defaultdict as dd, deque
from heapq import heappop, heapify


class DisjointSet:

    def __init__(self, elements):
        self.parent = [0] * elements
        self.size = [0] * elements
        for i in range(elements):
            self.make_set(i)

    def make_set(self, value):
        self.parent[value] = value
        self.size[value] = 1

    def find(self, value):
        if self.parent[value] != value:
            self.parent[value] = self.find(self.parent[value])
        return self.parent[value]

    def union(self, value1, value2):
        parent1, parent2 = self.find(value1), self.find(value2)
        if self.size[parent1] > self.size[parent2]:
            self.parent[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        else:
            self.parent[parent1] = parent2
            self.size[parent2] += self.size[parent1]


def kruskal(edge_list):
    mst = dd(set)
    while edge_list:
        weight, ver1, ver2 = heappop(edge_list)
        # Checking if adding the edge would make a cycle
        if dsu.find(ver1) == dsu.find(ver2):
            continue
        mst[ver1].add(ver2)
        mst[ver2].add(ver1)
        dsu.union(ver1, ver2)
    return mst


n, m = map(int, input("The number of vertices and number of edges.\n").split())
dsu = DisjointSet(n)
graph = dd(set)
edges = set()
weights = dd(set)
for i in range(m):
    u, v, w = map(int, input("Enter the edge with its weight.\n").split())
    graph[u].add(v)
    graph[v].add(u)
    # dsu.union(u, v)
    weights[(u, v)].add(w)
    weights[(v, u)].add(w)
for i in graph.keys():
    for j in graph[i]:
        # To add an edge only once.
        edges.add((min(weights[(i, j)]), min(i, j), max(i, j)))
edges = list(edges)
# Arranging edges according to their weight.
heapify(edges)
answer = kruskal(edges)
print("Required tree is", answer)
# 6 9
# 0 2 7
# 0 1 8
# 2 3 10
# 2 3 5
# 2 1 3
# 1 3 6
# 1 4 3
# 3 5 4
# 3 4 2
