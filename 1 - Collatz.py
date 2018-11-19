# This program applies Collatz to a number entered by the user.

def collatz(number):
    if number%2 == 0:
        return number//2
    else:
        return 3 * number + 1

print('Enter number:')
n = None
while n == None:
    try:
        n = int(input())
    except ValueError:
        print('You must enter an integer. Try again.')
while n != 1:
    n = collatz(n)
    print(n)