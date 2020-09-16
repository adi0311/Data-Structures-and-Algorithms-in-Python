class Deque:
    class _Node:
        __slots__ = '_data', '_next'
        def __init__(self, value, address):
            self._data = value
            self._next = address
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def is_empty(self):
        return self._size == 0
    def add_first(self, value):
        new_node = self._Node(value, None)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next = self._head
        self._head = new_node
        self._size += 1
    def add_last(self, value):
        new_node = self._Node(value, None)
        if self.is_empty():
            self._head = new_node
            self._tal = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1
    def remove_first(self):
        if self.is_empty():
            raise IndexError
        value = self._head._data
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return value
    def remove_last(self):
        if self.is_empty():
            raise IndexError
        value = self._tail._data
        temp = self._head
        i = 1
        while i < self._size-1:
            temp = temp._next
            i += 1
        self._tail = temp
        self._tail._next = None
        self._size -= 1
        if self.is_empty():
            self._head = None
        return value
    def printdeque(self):
        temp = self._head
        while temp:
            print(temp._data, end='-->')
            temp = temp._next
        print()


dll = Deque()
dll.add_first(2)
dll.add_first(1)
dll.add_last(3)
dll.add_last(4)
dll.printdeque()
print(dll.remove_first())
dll.printdeque()
print(dll.remove_last())
dll.printdeque()
print(dll.remove_last())
dll.printdeque()
print(dll.remove_last())
dll.printdeque()
