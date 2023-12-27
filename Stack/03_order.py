from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)

    def deque(self):
        if len(self.container) == 0:
            print("Empty Queue")
        return self.container.pop()
    
    def pop(self):
        return self.container.pop()
    
    def size(self):
        return len(self.container)
    
    def display(self):
        return self.container
    
q = Queue()


orders = ['Samosa', 'Kachori', 'Chhole', 'Poha']


for food in orders:
    q.enqueue(food)
    print( q.display() )


print( q.display() )

# q.deque()

print( q.display() )