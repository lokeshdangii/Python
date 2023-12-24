from collections import deque

class stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def peek(self):
        return self.container[-1]

    def pop(self):
        return self.container.pop()

    def size(self):
        return len(self.container)

    def printt(self):
        print(self.container)

    def p(self):
        print(deque())


str = input("Enter string: ")
stack_obj = stack()

for char in str:
    stack_obj.push(char)
stack_obj.printt()

size = stack_obj.size()
while(size > 1):
    print(stack_obj.pop())

stack_obj.printt()


