class Stacks:
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


    def push(self, value):
        new_node = self._Node(value, None)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next = self._head
        self._head = new_node
        self._size += 1


    def pop(self):
        if self.is_empty():
            print("The Stack is empty")
        else:
            value = self._head._data
            self._head = self._head._next
            self._size -= 1
            if self.is_empty():
                self._tail = None
            return value


    def top(self):
        return self._head._data


    def printlist(self):
        temp = self._head
        while temp:
            print(temp._data, end='-->')
            temp = temp._next
        print()


stack = Stacks()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.top())
stack.printlist()
print(stack.pop())
stack.printlist()
print(stack.pop())
stack.printlist()
print(stack.pop())
stack.printlist()
