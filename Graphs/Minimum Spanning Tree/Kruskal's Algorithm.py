"""
    Kruskal's Algorithm is greedy algorithm to get the
    Minimum Spanning Tree(MST) of the given weighted graph.
    MST is the tree with minimum weight.
    Kruskal's Algorithm greedily selects the edge with the
    minimum weight and adds it to the MST if it does not
    create cycle with already added edges, otherwise it
    discards that edge.
    Time Complexity :- O(V + E log E), because we sort
    the edges by weight.
    V -> Number of Vertices.
    E -> Number of Edges.
"""


class DisjointSet:

    def __init__(self, elements):
        self.parent = [value for value in range(elements)]
        self.size = [1] * elements

    def find(self, value):
        if self.parent[value] != value:
            self.parent[value] = self.find(self.parent[value])
        return self.parent[value]

    def union(self, value1, value2):
        parent1, parent2 = self.find(value1), self.find(value2)
        # If cycle is detected
        if parent1 == parent2:
            return True
        if self.size[parent1] > self.size[parent2]:
            parent1, parent2 = parent2, parent1
        self.parent[parent1] = parent2
        self.size[parent2] += self.size[parent1]
        # No cycle is detected
        return False


def kruskal(edge_list):
    mst = [list() for i in range(n)]
    for weight, ver1, ver2 in edge_list:
        # Checking if adding the edge would make a cycle
        if dsu.union(ver1, ver2):
            continue
        mst[ver1].append(ver2)
        mst[ver2].append(ver1)
    return mst


n, m = map(int, input("The number of vertices and number of edges.\n").split())
dsu = DisjointSet(n)
graph = [list() for i in range(n)]
edges = list()
for i in range(m):
    u, v, w = map(int, input("Enter the edge with its weight.\n").split())
    graph[u].append([v, w])
    graph[v].append([u, w])
    edges.append((w, u, v))
# Arranging edges according to their weight.
edges.sort(key=lambda x: x[0])
answer = kruskal(edges)
print("Required tree is", answer)
