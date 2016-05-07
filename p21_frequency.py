# Write a function char_freq() that takes a string
# and builds a frequency listing of the characters
# contained in it. Represent the frequency listing
# as a Python dictionary. Try it with something
# like char_freq("abbabcbdbabdbdbabababcbcbab").


def char_freq(a_string):
    freq = {}
    for cha in a_string:
        if not cha in freq.keys(): freq[cha] = a_string.count(cha)
    return freq

print(char_freq("abbabcbdbabdbdbabababcbcbab"))
print(char_freq("abcdef"))
print(char_freq("The quick brown fox jumps over the lazy dog"))