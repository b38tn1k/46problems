# Write a function translate() that will translate
# a text into "rovarspraket" (Swedish for
# "robber's language"). That is, double every
# consonant and place an occurrence of "o" in
# between. For example, translate("this is fun")
# should return the string "tothohisos isos
# fofunon".


def is_vowel(h): # using 'a' or 'i' or 'x' felt to definitive: https://en.wikipedia.org/wiki/Voiceless_glottal_fricative
    vowels = 'aeiouAEIOU'
    if type(h) is str:                  # is it a string?
        if h.isalpha() and len(h) == 1: # is it a character (i.e.a string of length 1)?
            if h in vowels: return True # is it a vowel?
    return False

def translate(string):
    new_string = ""
    for letter in string:
        if not is_vowel(letter) and not letter == ' ':
            new_string += letter + 'o' + letter.lower()
        else: new_string += letter
    return new_string

print(translate('this is fun'))

print(translate('this is fun') == "tothohisos isos fofunon")