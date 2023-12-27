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
        print(self.container)
        return self.container


# instantiating three stack towers
tower_1 = Stack()
tower_2 = Stack()
tower_3 = Stack()

# intial state 
tower_1.push('C')
tower_1.push('B')
tower_1.push('A')
# printing initial state
print("---------------- Tower 3 ----------------------\n")
tower_1.display()

# Step1 -> Moving A to tower 3
tower_3.push(tower_1.pop())

# Step2  -> Moving B to tower2 
tower_2.push(tower_1.pop())

# Step3 -> Moving A to tower2
tower_2.push(tower_3.pop())

# Step4 -> Moving C to tower3 
tower_3.push(tower_1.pop())

# step5 -> Moving A to tower1
tower_1.push(tower_2.pop())

# step6 -> Moving B  to tower3 
tower_3.push(tower_2.pop())

# step7 -> Moving A to tower 3
tower_3.push(tower_1.pop())


# printing
print("\n---------------- Tower 3 ----------------------\n")
tower_3.display()





