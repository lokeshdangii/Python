rom collections import deque

class Stack:
    def _init_(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def peek(self):
        return self.container[-1]
    
    def pop(self):
        return self.container.pop()
    
    def size(self):
        return len(self.container)
    
    def display(self):
        return self.container
    
stackObj1 = Stack()
stackObj2 = Stack()
stackObj3 = Stack()


array = [ num for num in range(1, 101)  ]

for num in range(len(array)):
    
    if num < 33:
        stackObj1.push(array[num])

    if num >33 and num < 66 :
        stackObj2.push(array[num])

    if num > 66:
        stackObj3.push(array[num])


print(stackObj1.display())
print(stackObj2.display())
print(stackObj3.display())