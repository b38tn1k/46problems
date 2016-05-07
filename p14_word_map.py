# Write a program that maps a list of words into a
# list of integers representing the lengths of the
# corresponding words.


def word_map(word_list):
    return list(map(len, word_list))

print(word_map(['dog', 'cat', 'rain', 'fish']))