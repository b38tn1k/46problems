# Write a function filter_long_words() that takes
# a list of words and an integer n and returns the
# list of words that are longer than n.


def filter_long_words(word_list, n):
    return [x for x in word_list if len(x) > n]

def filter_long_words_with_a_filter(word_list, n):
    return list(filter(lambda x: len(x) > n, word_list)) # filter returns an iterator

print(filter_long_words(['dog', 'cat', 'rain', 'fisherman'], 3))
print(filter_long_words_with_a_filter(['dog', 'cat', 'rain', 'fisherman'], 3))