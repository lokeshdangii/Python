year = int(input('Enter year: '))

# Checking for loop and taking decision
if (year%400==0) or (year%4==0 and year%100!=0):
    print('LEAP YEAR')
else:
    print('NOT LEAP YEAR')