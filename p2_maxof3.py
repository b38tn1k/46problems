from functools import reduce
# Define a function max_of_three() that takes
# three numbers as arguments and returns the
# largest of them.

# GENERAL SOLUTION
def max_of_n(* numbers):
    return reduce(lambda a, b: a if (a > b) else b, numbers)
# MUST ONLY WORK FOR 3 ARGS

# LAZY SOLUTION
def maxlazy3(x, y, z):
    def max2(a, b): # PROBLEM 1: CMD-C CMD-V
        if a > b: return a
        else: return b
    return(max2(max2(x, y), z))

# EXPECTED SOLUTION
def max_of_3(a, b, c):
    if a > b > c: return a
    elif b > c > a:return b
    else: return c

# OBSTINATE SOLUTION
def max3(* numbers):
    if not len(numbers) == 3: return 'ERROR!' # exit()
    else: return reduce(lambda a, b: a if (a > b) else b, numbers)

print(max_of_n(2, 4, 5, 6, 4, 6, 4, 2))
print(max_of_n(2, 4, 5, 6, 4, 60, 4, 2))
print(max_of_3(1, 2, 3))
print(max_of_3(1, 20, 3))
print(max_of_3(100, 20, 3))
print(max3(1, 2, 3))
print(max3(10, 2, 3))
print(max3(10, 2, 3, 5, 4, 34)) # ERROR!
print(maxlazy3(2, 3, 4))
print(maxlazy3(2, 3, 40))
print(maxlazy3(2, 30, 4))

