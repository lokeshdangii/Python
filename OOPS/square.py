class Square:
    def __init__(self):
        self.side = int(input("Enter Side:"))
    def area(self):
        a = self.side*self.side
        return a

sq1 = Square()
Area = sq1.area()
print("Area : ",Area)