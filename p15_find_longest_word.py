# Write a function find_longest_word() that takes
# a list of words and returns the length of the
# longest one.


def find_longest_word(word_list):
    return max(list(map(len, word_list)))

print(find_longest_word(['dog', 'cat', 'rain', 'fish']))
print(find_longest_word(['dog', 'cat', 'rain', 'fisherman']))