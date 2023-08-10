#  Python program to print asterisk hour glass pattern

num_of_rows = int(input('Enter the value of n: '))

for row in range(1,2*num_of_rows):
    for column in range(1,2*num_of_rows):
        if row==num_of_rows or row==column or row+column==2*num_of_rows:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()