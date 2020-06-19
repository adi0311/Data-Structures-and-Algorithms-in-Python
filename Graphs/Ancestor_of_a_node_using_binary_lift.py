"""
    We will use binary lifing to get the i-th ancestor of a given node.
    The pre computing time for the table is O(n log n) and time for each query
    is O(log n).
    The concept is simple, when power of 2 is 0 i.e. node one above the given node.
    This is the base case and we will assign the parents with a simple dfs.
    Now for computation of other powers of 2, we will use the concept that
    2^(i-1) + 2^(i-1) = 2^i. Therefore, if parent to 2 ^ (i-1) is known and from that node,
    2 ^ (i-1)th parent is known we can easily calculate for any i.
    Recurrence relation will be:-
    1. When i = 0, table[0][j] = parent[j] -> where i is the power of 2 and j is the nodes.
    2. When i > 0, table[i][j] = table[i-1][table[i-1][j]] -> parent(2^i) = parent((parent, 2^(i-1)), 2^(i-1))
"""

from collections import defaultdict as dd
from math import log


def dfs(source, par=-1):
    for child in graph[source]:
        if child != par:
            parent[child] = source
            dfs(child, source)


def precompute():
    dfs(0)  # Considering 0 as the root of the tree.
    for i in range(lg+1):
        for j in range(n):
            if i == 0:
                table[i][j] = parent[j]
                continue
            table[i][j] = table[i-1][table[i-1][j]]


n, m = map(int, input().split())    # The number of nodes and number of edges
graph = dd(set)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)
lg = int(log(n, 2))
# To pre compute the parents of nodes at a distance of powers of two.
parent = dd(lambda: -1)
table = dd(lambda: dd(lambda: -1))
precompute()
node, ancestor = map(int, input().split())  # Enter the node and i-th ancestor we want to find
for i in range(lg+1):
    if ancestor & 1:
        node = table[i][node]
    ancestor >>= 1
print(node)
