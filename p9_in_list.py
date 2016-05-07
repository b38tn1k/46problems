# Write a function is_member() that takes a value
# (i.e. a number, string, etc) x and a list of
# values a, and returns True if x is a member of
# a, False otherwise. (Note that this is exactly
# what the in operator does, but for the sake of
# the exercise you should pretend Python did not
# have this operator.)


def is_member(a_value, a_list):
        for value in a_list:
            if a_value == value: return True
        return False

print(is_member('dog', ['dog', 'cat', 'rain', 'fish']))
print(is_member('llama', ['dog', 'cat', 'rain', 'fish']))
print(is_member(2, [1, 2, 3, 4]))
print(is_member(5, [1, 2, 3, 4]))