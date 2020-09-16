"""
    White-Gray-Black DFS is a common coloring technique
    in a Directed to Graph to detect cycles.
"""


from collections import defaultdict as dd


def white_gray_black_dfs(source):
    # Assigning initial color as Gray to the source node.
    color[source] = 1
    for child in graph[source]:
        # If the color of child node is similar to source node
        if color[child] == 1:
            return True
        # If child is not visited yet and after visiting it gives grey color
        if not color[child] and white_gray_black_dfs(child) == 1:
            return True
    # source is not included in a cycle, so assign black color.
    color[source] = 2
    return False


n, m = map(int, input("Enter the number of nodes and edges:\n").split())
graph = dd(set)
for i in range(m):
    u, v = map(int, input("Enter the to-from edge:\n").split())
    graph[u].add(v)

# 0 - White, 1 - Gray, 2 - Black
color = [0] * n
for i in range(n):
    # If the node is not visited yet
    if not color[i]:
        white_gray_black_dfs(i)
non_cyclic_nodes = []
for i in range(n):
    # If they are black, add them to the non_cyclic nodes
    if color[i] == 2:
        non_cyclic_nodes.append(i)
print(non_cyclic_nodes)
