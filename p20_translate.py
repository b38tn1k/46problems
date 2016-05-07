# Represent a small bilingual lexicon as a Python
# dictionary in the following fashion
# {"merry":"god", "christmas":"jul", "and":"och",
# "happy":gott", "new":"nytt", "year":"år"} and
# use it to translate your Christmas cards from
# English into Swedish. That is, write a function
# translate() that takes a list of English words
# and returns a list of Swedish words.


my_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}


def translator(sentence):
    sentence = sentence.split()
    t_sentence = []
    for word in sentence:
        if word in my_dict.keys(): t_sentence.append(my_dict[word])
        else: t_sentence.append(word)
    return " ".join(t_sentence)


print (translator('merry christmas and a happy new year'))