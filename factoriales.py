# import sys
# sys.setrecursionlimit(1000)
# print(sys.getrecursionlimit())

def factorial(n):
    """Calculate n factorial
    n int > 0
    returns n!
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input('Input a integer to get the factorial value: '))
print(f'{n} factorial = {factorial(n)}')
