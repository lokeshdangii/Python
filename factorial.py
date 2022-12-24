x = int(input("Enter no. : "))
y = 1

for i in range(x+1,1,-1):
    y = y*i
print("Factorial of {} is {}". format(x,y))