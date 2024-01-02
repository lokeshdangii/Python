from collections import deque

class Stack:
    def __init__(self):
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


stack1 = Stack()  # main stack
stack2 = Stack()  #stack to store elements temporarily

numbers = int(input("Enter no. of elements to store in stack : "))

for i in range(numbers):
    element = int(input("Enter element to store in stack : "))

    # if element is greater than push directly
    if stack1.size() > 0 and element > stack1.peek():
        stack1.push(element)
        print(stack1.display())

    # if element is small than the top element of stack1 
    elif stack1.size() > 0 and element < stack1.peek():
        
        # first pop and push those elements to stack2
        while(stack1.size() > 0 and stack1.peek() > element):
            stack2.push(stack1.pop())

        stack1.push(element)
        print(stack1.display())

        # again pushing the elements of stack2 to stack1
        while(stack2.size() > 0):
            stack1.push(stack2.pop())
            print(stack1.display())

    # condition to push the first element in the stack
    elif stack1.size() == 0:
        stack1.push(element)
        print(stack1.display())


print(stack1.display())