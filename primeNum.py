
print('This is a simple program to find a prime number. Click E to exit')

while True:
    try:
        num = input('\nEnter a number: ')
        if num.lower() == 'e':
            print('Program exits')
            break
        else:
            num = int(num)
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print('{} is not a prime number'.format(num))
                    break
            else:
                print('{} is a prime number'.format(num))
        else:
            print('{} is not a prime number'.format(num))
    except ValueError:
        print('Please enter an integer')
        continue