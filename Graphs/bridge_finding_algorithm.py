"""
    Bridges are those edges, whose removal from the
    graph causes the graph to disconnect.
"""


def dfs(source, parent):
    global id, bridges
    vis[source] = True
    ids[source] = low[source] = id
    id += 1
    for child in graph[source]:
        if child == parent:
            continue
        if not vis[child]:
            dfs(child, source)
            low[source] = min(low[source], low[child])
            if ids[source] < low[child]:
                bridges.append([source, child])
        else:
            low[source] = min(low[source], ids[child])


n = int(input("Enter the number of vertices\n"))
m = int(input("Enter the number of edges\n"))
graph = [list() for i in range(n)]
for i in range(m):
    u, v = map(int, input("Enter edge:\n").split())
    graph[u].append(v)
    graph[v].append(u)
ids = [-1] * n
low = [-1] * n
vis = [False] * n
id = 0
bridges = []
for i in range(n):
    if not vis[i]:
        dfs(i, -1)
print(bridges)
