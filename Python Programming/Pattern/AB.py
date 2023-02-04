n = int(input("Enter number of rows: "))

for i in range(1,n+1):
    a = 65
    for j in range(1, i+1):
        print("%c" %(a), end="")
        a +=1
    print()