from collections import deque

class queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self,val):
        self.container.appendleft(val)

    def peek(self):
        return self.container[-1]

    def dequeue(self):
        if len(self.container) == 0:
            print("Empty")
        return self.container.pop()

    def size(self):
        return len(self.container)

    def printt(self):
        print(self.container)

    def p(self):
        print(deque())


# queue object
q = queue()
q.printt()

q.appendleft(1)
q.appendleft(2)
q.appendleft(3)
q.appendleft(4)

q.printt()




