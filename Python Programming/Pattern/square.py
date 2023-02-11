row = int(input("Enter number of rows: "))

print("Square pattern is: ")
for i in range(1,row+1):
    for j in range(1,row+1):
        print("*", end="")
    print()