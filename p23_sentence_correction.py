# Define a simple "spelling correction" function
# correct() that takes a string and sees to it
# that 1) two or more occurrences of the space
# character is compressed into one, and 2) inserts
# an extra space after a period if the period is
# directly followed by a letter. E.g.
# correct("This   is  very funny  and
# cool.Indeed!") should return "This is very funny
# and cool. Indeed!" Tip: Use regular expressions!


import re


def correct(a_string):
    corrected = re.sub("\s+", " ", a_string)
    corrected = re.sub("(\.)\s*", ". ", corrected)
    return corrected



print(correct("This   is  very funny  and    cool.Indeed!"))