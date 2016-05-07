from functools import reduce
# Define a function sum() and a function
# multiply() that sums and multiplies
# (respectively) all the numbers in a list of
# numbers. For example, sum([1, 2, 3, 4]) should
# return 10, and multiply([1, 2, 3, 4]) should
# return 24.


def sum(numbers):
    return reduce((lambda a, b : a + b), numbers)

def multiply(numbers):
    return reduce((lambda a, b : a * b), numbers)

print(sum([1, 2, 3, 4]) == 10)

print(multiply([1, 2, 3, 4]) == 24)