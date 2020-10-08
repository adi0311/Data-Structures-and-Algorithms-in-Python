class Stack:
    def __init__(self):
        self.q = Queue()
 
    def is_empty(self):
        return self.q.is_empty()
 
    def push(self, data):
        self.q.enqueue(data)
 
    def pop(self):
        for _ in range(self.q.get_size() - 1):
            dequeued = self.q.dequeue()
            self.q.enqueue(dequeued)
        return self.q.dequeue()
 
 
class Queue:
    def __init__(self):
        self.items = []
        self.size = 0
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.size += 1
        self.items.append(data)
 
    def dequeue(self):
        self.size -= 1
        return self.items.pop(0)
 
    def get_size(self):
        return self.size
 
 
s = Stack()
 
print('Menu')
print('push <value>')
print('pop')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        break
