"""
    >>> G = Graph(6)
    >>> G.insert(0, 1, 3)
    >>> G.insert(0, 2, 7)
    >>> G.insert(0, 4, 8)
    >>> G.insert(0, 5, 1)
    >>> G.insert(1, 2, 2)
    >>> G.insert(1, 4, 13)
    >>> G.insert(2, 3, 15)
    >>> G.insert(3, 5, 17)
    >>> G.insert(4, 5, 9)
    >>> G.dijkstra(0)[0]
    [0, 3, 5, 20, 8, 1]
    >>> G.shortest_distance(0, 3)
    [0, 1, 2, 3]
"""
"""
    !!!!! Not yet completed. Still in progress !!!!!
    Eager Implementation is better than the Lazy Implementation
    because duplicate pair of (node, distance) doesn't exist.
    Index based Priority Queue is used to implement Dijkstra's Algorithm Eagerly.
"""

from sys import maxsize
from collections import deque


class Graph:
    def __init__(self, vertices):
        self.adjmat = dict()
        self.vertices = vertices
        for i in range(vertices):
            self.adjmat[i] = dict()

    def insert(self, u, v, w=1):
        # Vertex from u to v because it is a directed graph
        self.adjmat[u][v] = w

    def dijkstra(self, source):
        vis = [False for i in range(self.vertices)]
        dist = [maxsize for i in range(self.vertices)]
        prev = [None for i in range(self.vertices)]
        dist[source] = 0
        pq = deque()
        pq.append((source, 0))
        while len(pq) > 0:
            node, mindist = pq.popleft()
            vis[node] = True
            if dist[node] < mindist:
                continue
            for i in self.adjmat[node].keys():
                if vis[i]:
                    continue
                new_dist = dist[node] + self.adjmat[node][i]  # Add present distance with weight of the edge
                if new_dist < dist[i]:  # If better path is found
                    prev[i] = node
                    dist[i] = new_dist
                    pq.append((i, new_dist))
            pq = sorted(pq, key=lambda x: x[1])  # Sort according to the distance
            pq = deque(pq)
        return dist, prev  # Return minimum distance of each node from source.

    def shortest_distance(self, s, e):
        dist, prev = self.dijkstra(s)
        path = list()
        if dist[e] == maxsize:
            return path
        i = e
        while i is not None:
            path.append(i)
            i = prev[i]
        return path[::-1]
