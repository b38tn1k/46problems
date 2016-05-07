# Define a function reverse() that computes the
# reversal of a string. For example, reverse("I am
# testing") should return the string "gnitset ma
# I".


def reverse(a_string):
    return a_string[::-1]   # [begin:end:step]

print(reverse("I am testing"))