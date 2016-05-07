# Define a function overlapping() that takes two
# lists and returns True if they have at least one
# member in common, False otherwise. You may use
# your is_member() function, or the in operator,
# but for the sake of the exercise, you should
# (also) write it using two nested for-loops.


def overlapping(a_list, b_list):
    for a_value in a_list:
        for b_value in b_list:
            if a_value is b_value: return True
    return False

print(overlapping(['llama', 'dog'], ['dog', 'cat', 'rain', 'fish']))
print(overlapping(['llama', 'alpaca'], ['dog', 'cat', 'rain', 'fish']))