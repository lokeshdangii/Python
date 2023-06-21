# Generating Right Angle Triangle Pattern Using Stars

row = int(input('Enter number of rows required: '))

for i in range(row):
    for j in range(i+1):
        print('*',end=' ')
    print()