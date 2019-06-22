class heaps:

    def __init__(self, n):
        self._maxsize = n
        self._data = [-1]*n
        self._size = 0

    def __len__(self):
        return len(self._data)

    def max(self):
        if self._size == 0:
            raise IndexError
        return self._data[1]

    def insert(self, value):
        if self._size == self._maxsize:
            raise IndexError
        self._size += 1
        i = self._size
        while i != 1 and value > self._data[i//2]:
            self._data[i] = self._data[i//2]
            i = i//2
        self._data[i] = value
    def delete(self):
        if self._size == 0:
            raise IndexError
        max = self._data[1]
        min = self._data[self._size]
        self._size -= 1
        i = 1
        ci = 2
        while ci <= self._size:
            if ci < self._size and self._data[ci] < self._data[ci+1]:
                ci += 1
            if min >= self._data[ci+1]:
                break
            self._data[i] = self._data[ci]
            i = ci
            ci = ci*2
        self._data[self._size+1] = -1
        self._data[i] = min
        return max


heap = heaps(10)
heap.insert(25)
heap.insert(14)
heap.insert(2)
heap.insert(20)
heap.insert(10)
heap.insert(12)
print(heap._data)
print(heap.delete())
print(heap._data)
print(heap.delete())
print(heap._data)
print(heap.delete())
print(heap._data)