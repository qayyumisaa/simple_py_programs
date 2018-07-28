
def numInput():
    global num1, num2
    while True:
        try:
            num1 = int(input('\nEnter first number: '))
            break
        except ValueError:
            print('Please enter an integer!')
            continue
    while True:
        try:
            num2 = int(input('\nEnter second number: '))
            break
        except ValueError:
            print('Please enter an integer!')
            continue
    


def addition(num1, num2):
    print('%s + %s = %s' % (str(num1), str(num2), str(num1 + num2)))

def subtraction(num1, num2):
    print('%s - %s = %s' % (str(num1), str(num2), str(num1 - num2)))

def division(num1, num2):
    print('%s / %s = %s' % (str(num1), str(num2), str(num1 / num2)))

def multiplication(num1, num2):
    print('%s x %s = %s' % (str(num1), str(num2), str(num1 * num2)))

print('\nClick A/B/C/D:\nA. Additon\nB. Subtraction\nC. Division\nD. Multiplication')

while True:
    calculation_choice = input('\nChoose an operation: ').lower()

    if calculation_choice == 'a' or 'b' or 'c' or 'd':  
        if calculation_choice == 'a':
            numInput()
            addition(num1, num2)
            break
        elif calculation_choice == 'b':
            numInput()
            subtraction(num1, num2)
            break
        elif calculation_choice == 'c':
            numInput()
            division(num1, num2)
            break
        elif calculation_choice == 'd':
            numInput()
            multiplication(num1, num2)
            break
        else:
            print('Click a valid selection')
    else:
        print('Click a valid selection')
        continue

