

def find_factorial(num):
    factorial = 1
    if num < 0:
        print('Factorial does not exist for negative number.')
    elif num == 0:
        print('The factorial for 0 is 1')
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print('The factorial for ' + str(num) + ' is ' + str(factorial))

num = int(input('Enter a number: '))
find_factorial(num)
        