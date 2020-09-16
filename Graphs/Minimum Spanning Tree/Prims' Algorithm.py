"""
    Prims' Algorithm is greedy algorithm to get the
    Minimum Spanning Tree(MST) of the given weighted graph.
    MST is the tree with minimum weight.
    Prims' Algorithm greedily selects the edge with the
    minimum weight and adds it to the MST if it does not
    create cycle with already added edges, otherwise it
    discards that edge.
    Time Complexity :- O(V + E log E), because we sort
    the edges by weight.
    V -> Number of Vertices.
    E -> Number of Edges.
"""


from heapq import heappop, heappush


class DisjointSet:

    def __init__(self, elements):
        self.parent = [i for i in range(elements)]
        self.size = [1] * elements

    def find(self, value):
        if value != self.parent[value]:
            self.parent[value] = self.find(self.parent[value])
        return self.parent[value]

    def union(self, value1, value2):
        parent1, parent2 = self.find(value1), self.find(value2)
        if parent1 == parent2:
            return True
        if self.size[parent2] > self.size[parent1]:
            parent2, parent1 = parent1, parent2
        self.size[parent1] += self.size[parent2]
        self.parent[value2] = self.parent[value2] = parent1
        return False


def bfs(source):
    tree = [list() for i in range(n)]
    dsu = DisjointSet(n)
    edges = []
    for child, weight in graph[source]:
        heappush(edges, [weight, source, child])
    while edges:
        weight, source, child = heappop(edges)
        if dsu.union(source, child):
            continue
        tree[source].append(child)
        tree[child].append(source)
        for grandchild, weight in graph[child]:
            if grandchild == source:
                continue
            heappush(edges, [weight, child, grandchild])
    return tree


n = int(input("Enter the number of vertices:-\n"))
graph = [list() for i in range(n)]
m = int(input("Enter the number of edges:-\n"))
for i in range(m):
    u, v, w = map(int, input("Enter first vertex, second vertex and weight:-\n").split())
    graph[u].append([v, w])
    graph[v].append([u, w])
mst = bfs(0)
print("Minimum Spanning Tree is:-", mst)

# 6
# 8
# 0 1 8
# 0 2 7
# 1 3 6
# 1 2 3
# 1 4 3
# 2 3 5
# 3 4 2
# 3 5 4
