from collections import defaultdict as dd
from math import log2


def dfs(source, par=0):
    parent[source][0] = par # The ancestor of source at a lift of 1 is parent itself.
    for i in range(1, lg):
        parent[source][i] = parent[parent[source][i-1]][i-1]
    for child in tree[source]:
        if child != par:
            level[child] = level[source] + 1
            dfs(child, source)


def calculate_lca(node1, node2):
    if level[node1] < level[node2]:
        node1, node2 = node2, node1
    height_diff = level[node1] - level[node2]
    # We will lift node1 to the level of node2
    for i in range(lg):
        if height_diff & (1 << i):
            node1 = parent[node1][i]
    # node2 is the LCA in this case.
    if node1 == node2:
        return node1
    # Lift both nodes until their parents become the same
    for i in range(lg-1, -1, -1):
        if parent[node1][i] != parent[node2][i]:
            node1 = parent[node1][i]
            node2 = parent[node2][i]
    # Parent of both node1 and node is same now. Return any of the parent of node1 or node2.
    return parent[node1][0]


tree = dd(set)
# We will consider nodes numbered from 1 to n.
n = int(input("Enter the number of nodes.\n"))
# m is the number of edges which is obviously n-1 for a tree
m = n-1
for _ in range(m):
    u, v = map(int, input("Pair of node with edge b/w them.\n").split())
    tree[u].add(v)
    tree[v].add(u)
lg = int(log2(n)+1)
level = dd(int)
parent = dd(lambda: dd(int))
dfs(1)
u, v = map(int, input("Enter two nodes to know their lca.\n").split())
print(calculate_lca(u, v))
