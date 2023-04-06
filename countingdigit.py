def count_digit(n):
    count = 0
    while n:
        n //= 10
        count += 1

    return count

# Read number
number = int(input('Enter number: '))

print('Number of digit in %d is %d.' %(number, count_digit(number)))