"""
    To detect a cycle in an undirected graph we need to keep a visited array or set(which is preferable).
    We will do DFS from an unvisited node. In dfs if some node is already present in visited set and
    it is not equal to the parent of current node. Then there must be a cycle. Therefore we will return True.
    Otherwise, we will return False.
"""
from collections import defaultdict as dd


def dfs(source, parent):
    vis[source] = True
    for child in graph[source]:
        # Cycle is detected in this case.
        if vis[child] and child != parent:
            cycle_present[0] = True
            return
        if not vis[child]:
            dfs(child, source)


# The nodes will be numbered 1 to n.
n = int(input("Enter the number of vertices in the graph: "))
graph = dd(set)
m = int(input("Enter the number of edges in the graph: "))
for i in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
vis = dd(lambda: False)
cycle_present = [False]
for i in range(1, n+1):
    # A for loop is required in case of disconnected components in graph.
    if not vis[i]:
        dfs(i, 0)
        if cycle_present[0]:
            print("Cycle is present in the graph.")
            exit()
print("Cycle is not present in the graph.")
