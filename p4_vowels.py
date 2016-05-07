# Write a function that takes a character (i.e. a
# string of length 1) and returns True if it is a
# vowel, False otherwise.


def is_vowel(h): # using 'a' or 'i' or 'x' felt to definitive: https://en.wikipedia.org/wiki/Voiceless_glottal_fricative
    vowels = 'aeiouAEIOU'
    if type(h) is str:                  # is it a string?
        if h.isalpha() and len(h) == 1: # is it a character (i.e.a string of length 1)?
            if h in vowels: return True # is it a vowel?
    return False

print(is_vowel(1))       # FALSE
print(is_vowel('f'))     # FALSE
print(is_vowel('a'))     # TRUE
print(is_vowel('I'))     # TRUE
print(is_vowel('L'))     # FALSE
print(is_vowel('Evil'))  # FALSE
