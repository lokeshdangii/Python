# program to print inverted star pyramid

row = int(input('Enter number of rows required: '))

# loop for line
for i in range(row,0,-1):
    
    # loop for spaces
    for j in range(row-i):
        print(' ', end='') 
    
    # loop for stars
    for j in range(2*i-1):
        print('*',end='') 
    print() #next line