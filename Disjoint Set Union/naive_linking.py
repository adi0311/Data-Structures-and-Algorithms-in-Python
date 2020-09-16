class DisjointSet:

    def __init__(self, elements):
        self.parent = [0] * elements

    def make_set(self, value):
        self.parent[value] = value

    def find(self, value):
        while self.parent[value] != value:
            value = self.parent[value]
        return value

    def union(self, value1, value2):
        parent1, parent2 = self.find(value1), self.find(value2)
        self.parent[parent1] = parent2


d = DisjointSet(8)
for i in range(8):
    d.make_set(i)
d.union(1, 2)
d.union(2, 3)
d.union(4, 5)
print(d.find(2))
print(d.find(4))
d.union(2, 4)
print(d.find(3))
