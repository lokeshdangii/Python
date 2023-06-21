first = float(input('Enter first number: '))
second = float(input('Enter second number: '))

if first < second:
    small = first
else:
    small = second

print('Smallest = %d' %(small))