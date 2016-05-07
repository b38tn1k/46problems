# Write a version of a palindrome recognizer that
# also accepts phrase palindromes such as "Go hang
# a salami I'm a lasagna hog.", "Was it a rat I
# saw?", "Step on no pets", "Sit on a potato pan,
# Otis", "Lisa Bonet ate no basil", "Satan,
# oscillate my metallic sonatas", "I roamed under
# it as a tired nude Maori", "Rise to vote sir",
# or the exclamation "Dammit, I'm mad!". Note that
# punctuation, capitalization, and spacing are
# usually ignored.


def is_grammarless_palindrome(a_string):
    stripped = list(x for x in a_string if x.isalpha())
    length = len(stripped)
    if length < 1: return True
    for i in range(int(length/2)):
        if  not stripped[i].lower() == stripped[length - (i + 1)].lower(): return False
    return True

print (is_grammarless_palindrome("Go hang a salami I'm a lasagna hog."))
print (is_grammarless_palindrome("Was it a rat I saw?"))
print (is_grammarless_palindrome("Step on no pets"))
print (is_grammarless_palindrome("Sit on a potato pan, Otis"))
print (is_grammarless_palindrome("Lisa Bonet ate no basil"))
print (is_grammarless_palindrome("Satan, oscillate my metallic sonatas"))
print (is_grammarless_palindrome("I roamed under it as a tired nude Maori"))
print (is_grammarless_palindrome("Rise to vote sir"))
print (is_grammarless_palindrome("Dammit, I'm mad!"))
print (is_grammarless_palindrome("!!THIS Sentence is NOT A PALINDRome!!"))