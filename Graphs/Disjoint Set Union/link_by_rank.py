class DisjointSet:

    def __init__(self, elements):
        self.parent = [0] * elements
        self.rank = [0] * elements

    def make_set(self, value):
        self.parent[value] = value
        self.rank[value] = 0

    def find(self, value):
        while self.parent[value] != value:
            value = self.parent[value]
        return value

    def union(self, value1, value2):
        parent1, parent2 = self.find(value1), self.find(value2)
        if self.rank[parent2] > self.rank[parent1]:
            self.parent[parent1] = parent2
        elif self.rank[parent1] > self.rank[parent1]:
            self.parent[parent2] = parent1
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] += 1


d = DisjointSet(8)
for i in range(8):
    d.make_set(i)
d.union(1, 2)
d.union(2, 3)
d.union(4, 5)
print(d.find(2))    # Will return 1
print(d.find(4))    # Will return 4
d.union(2, 4)
print(d.find(4))    #Will return 1
