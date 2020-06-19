"""
    If it is possible to color the graph in two colors such that
    no two adjacent nodes have same color than the given graph is
    bipartite.

    It can be achieved using a simple BFS where we assign 0 to uncolored node
    and subsequently assign opposite colors to all the neighbouring.
    If at any point two neighbouring nodes have same color than simply return False.
    Otherwise, simply return True.
"""

from collections import defaultdict as dd, deque


def is_bipartite():
    color = dd(lambda: -1)
    for i in range(1, n+1):
        if color[i] == -1:
            # Assigning color the uncolored vertex.
            color[i] = 0
            q = deque()
            q.append(i)
            while q:
                parent = q.popleft()
                for child in graph[parent]:
                    # If two neighbouring have same color, return False else continue.
                    if color[parent] == color[child]:
                        return False
                    if color[child] == -1:
                        # Coloring the uncolored neighbour in opposite color.
                        color[child] = 1 - color[parent]
                        q.append(child)
    return True


# Not Bipartite
n = 5   # Number of vertices.
m = 6   # Number of edges.
graph = dd(set)
graph[1] = {2, 4, 5}
graph[2] = {1, 3, 4}
graph[3] = {2}
graph[4] = {1, 2, 5}
graph[5] = {1, 4}
print(is_bipartite())


# Bipartite
n = 4
m = 5
graph = dd(set)
graph[1] = {2, 3}
graph[2] = {1, 4}
graph[3] = {1, 4}
graph[4] = {2, 3}
print(is_bipartite())
