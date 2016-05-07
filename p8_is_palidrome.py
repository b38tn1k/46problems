# Define a function is_palindrome() that
# recognizes palindromes (i.e. words that look the
# same written backwards). For example,
# is_palindrome("radar") should return True.


def is_palindrome(a_string):
    length = len(a_string)
    if length < 1: return True
    for i in range(int(length/2)):
        if  not a_string[i].lower() == a_string[length - (i + 1)].lower(): return False
    return True



hannah_gadsbys_family = ['Hannah', 'Mum', 'Dad', 'Nan', 'Pop', 'Kayak']     # https://youtu.be/t5ijqc5t6Sk?t=23s

print(is_palindrome('radar'))
print(is_palindrome('not radar'))
print(is_palindrome("what about this?"))
print(is_palindrome("a"))

for member in hannah_gadsbys_family:
    print(is_palindrome(member))