# python program to generate and print half pyramid pattern   

n = 5

# outer loop for line
for i in range(1,n):
    # inner loop to print numbers
    for j in range(1,i+1):
        print(j,end = " ")
    print("\r") #next line
