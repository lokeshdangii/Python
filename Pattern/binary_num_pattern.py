# Program to print the binary number pattern

lines = int(input("Enter number of lines of pattern: "))

# i denotes row
# j denotes column
# k is used to print only 0 & 1

for i in range(1,lines+1):
    for j in range(1, lines-i+1):
        print(" ", end="")
        
    for k in range(1,2*i):
        print(k%2, end="")
        
    print() #for next line