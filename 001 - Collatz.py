# This program applies Collatz to a number entered by the user.

def collatz(number):
    print(str(number))
    if number == 1:
        return
    else:
        return collatz(number//2 if number % 2 == 0 else 3 * number + 1)

print('Enter number: ', end='')
n = None
while n == None:
    try:
        n = int(input())
    except ValueError:
        print('You must enter an integer. Try again.')

collatz(n)
