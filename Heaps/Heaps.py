import sys


class Heaps:
    def __init__(self, n):
        self._maxsize = n
        self._data = [-1]*n
        self._size = 0

    def __len__(self):
        return len(self._data)

    def parent(self, i):
        return (i-1)//2

    def left_child(self, i):
        return 2*i+1

    def right_child(self, i):
        return 2*i+2

    def max(self):
        if self._size == 0:
            raise IndexError
        return self._data[0]

    def insert(self, value):
        if self._size == self._maxsize:
            raise IndexError
        self._size += 1
        self._data[self._size-1] = value
        i = self._size-1
        while i != 0 and self._data[self.parent(i)] < self._data[i]:
            self._data[self.parent(i)], self._data[i] = self._data[i], self._data[self.parent(i)]
            i = self.parent(i)

    def heapify(self, i):
        l = self.left_child(i)
        r = self.right_child(i)
        largest = i
        if l < self._size and self._data[l] > self._data[largest]:
            largest = l
        if r < self._size and self._data[r] > self._data[largest]:
            largest = r
        if i != largest:
            self._data[i], self._data[largest] = self._data[largest], self._data[i]
            self.heapify(largest)

    def extract_max(self):
        if self._size == 0:
            raise IndexError
        if self._size == 1:
            self._size -= 1
            return self._data[0]
        root = self._data[0]
        self._data[0] = self._data[self._size-1]
        self._data[self._size-1] = -1
        self._size -= 1
        self.heapify(0)
        return root

    def decrease_key(self, i, value):
        self._data[i] = value
        while i != 0 and self._data[self.parent(i)] < self._data[i]:
            self._data[self.parent(i)], self._data[i] = self._data[i], self._data[self.parent(i)]
            i = self.parent(i)

    def delete_key(self, i):
        if i >= self._size:
            print("Invalid Key")
            raise IndexError
        elif self._size == 0:
            print("Empty Heap")
            raise Exception
        self.decrease_key(i, sys.maxsize)
        self.extract_max()


heap = Heaps(10)
heap.insert(25)
heap.insert(14)
heap.insert(2)
heap.insert(20)
heap.insert(10)
heap.insert(12)
heap.insert(1)
heap.insert(30)
heap.insert(5)
heap.insert(8)
print(heap._data)
print(heap.max())
heap.delete_key(3)
print(heap._data)