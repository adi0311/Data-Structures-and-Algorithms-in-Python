from collections import defaultdict as dd


def dfs(source):
    vis[source] = 1
    ett.append(source)
    for child in graph[source]:
        if not vis[child]:
            dfs(child)
    ett.append(source)


graph = dd(set)
n = int(input())
for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
vis = [0] * (n+1)
ett = []
dfs(1)
print(ett)
