class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius

    def circumference(self):
        return 3.14 *2*self.radius

def dwrite(x):
    file1 = open("detail100.txt","a")
    file1.write(x)
    file1.close()

    # print("write operation done successfully")

def dread():
    data = open("detail100.txt", "r")
    data = data.read()
    record = data.split("\n")
    print("Data : ",record[i])
    print()
    print("-----------------")

    # data.close()

    
    # print("Area :",record[1])
    # print("Circumference :",record[2])
    
    # x = data.split("\n")

for i in range(1,101):
    var1 = circle(i)
    var2 = var1.area()
    var3 = var1.circumference()
    var4 = "{},{},{}\n".format(var1.radius,var2,var3)

    dwrite(var4)
    dread()
    # print("Radius of circle = {} cm".format(var1.radius))    
    # print("Area:{} sq cm".format(var2))
    # print("Circumference: {} cm".format(var3))
    # print("-------------------------------")







