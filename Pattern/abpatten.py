# Problem Statement:- Python program to print a half pyramid pattern of AB

row = int(input("Enter number of rows: "))

for row in range(1,row+1):
    # 65 is the ascii value of capital A
    ascii = 65 
    for column in range(1, row+1):
        print("%c" %(ascii), end="")
        ascii +=1  # ascii value of A is incremented every time to print A B accordingly
    print() # for next line