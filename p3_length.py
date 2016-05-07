# Define a function that computes the length of a
# given list or string. (It is true that Python
# has the len() function built in, but writing it
# yourself is nevertheless a good exercise.)


def length(thing):
    i = 0
    for bit in thing: i += 1
    return i

print(length("Hello"))
print(length(["Hello", "goodbye"]))