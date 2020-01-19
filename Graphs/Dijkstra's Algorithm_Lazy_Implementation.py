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
    >>> G.shortest_distance(1, 5)
    [1, 4, 5]
"""

"""
    Lazy implementation of Dijkstra's Algorithm.
    In this implementation we Lazily check all the (node, distance) pair
    even if a better distance for given node exists(i.e. duplicates exists).
    Priority queue which is always sorted in ascending order of distance.
"""

from sys import maxsize
import heapq
from collections import defaultdict as dd


class Graph:
    def __init__(self, vertices):
        # Using defaultdict to avoid key error
        self.adjmat = dd(dict)
        self.vertices = vertices
        for i in range(vertices):
            self.adjmat[i] = dd(int)

    def insert(self, u, v, w=1):
        # Vertex from u to v because it is a directed graph
        self.adjmat[u][v] = w

    def dijkstra(self, source):
        vis = [False for i in range(self.vertices)]
        dist = [maxsize for i in range(self.vertices)]
        prev = [None for i in range(self.vertices)]
        dist[source] = 0
        pq = list()
        pq.append((0, source))
        while len(pq) > 0:
            # Pop the node with shortest distance
            mindist, node = heapq.heappop(pq)
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
                    pq.append((new_dist, i))
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
