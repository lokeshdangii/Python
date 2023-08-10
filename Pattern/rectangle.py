# program to print the rectangle of stars

row = int(input("Enter number of rows: "))

print("Square pattern is: ")

# outer loop for lines 
for i in range(1,row+1):
    # inner loop to print stars
    for j in range(1,row+1):
        print("*", end="")
    print()