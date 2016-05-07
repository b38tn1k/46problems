# A pangram is a sentence that contains all the
# letters of the English alphabet at least once,
# for example: The quick brown fox jumps over the
# lazy dog. Your task here is to write a function
# to check a sentence to see if it is a pangram or
# not.


def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = 'The quick brown fox jumps over the lazy dog'.replace(" ", "").lower()
    for letter in sentence:
        if letter.lower() in alphabet: alphabet = alphabet.replace(letter, "")
    return len(alphabet) == 0

print (is_pangram("The quick brown fox jumps over the lazy dog"))
print (is_pangram("qwertyuiopasdfghjklzxcvbnm"))
print (is_pangram("this is not a parallelogram. I mean a pangram. yet. wait. what am I missing? z? b? It is more than one sentence anyway"))
print (is_pangram("This pangram contains four As, one B, two Cs, one D, thirty Es, six Fs, five Gs, seven Hs, eleven Is, one J, one K, two Ls, two Ms, eighteen Ns, fifteen Os, two Ps, one Q, five Rs, twenty-seven Ss, eighteen Ts, two Us, seven Vs, eight Ws, two Xs, three Ys, & one Z."))

