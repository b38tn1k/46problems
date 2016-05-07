# In English, the present participle is formed by
# adding the suffix -ing to the infinite form: go
# -> going. A simple set of heuristic rules can be
# given as follows:
#
# If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
# If the verb ends in ie, change ie to y and add ing
# For words consisting of consonant-vowel-consonant, double the final letter before adding ing
# By default just add ing
#
# Your task in this exercise is to define a
# function make_ing_form() which given a verb in
# infinitive form returns its present participle
# form. Test your function with words such as lie,
# see, move and hug. However, you must not expect
# such simple rules to work for all cases.


import re

def present_paticiple(a_string):
    ing = 'ing'
    if a_string.endswith('e') and len(a_string) > 2 and not (a_string.endswith('ee') or a_string.endswith('ie')): return a_string[:-1] + ing
    elif a_string.endswith('ie'): return a_string[:-2] + 'y' + ing
    elif re.match('([bcdfghjklmnpqrstvwxz][aeiou][bcdfghjklmnpqrstvwxz])+', a_string): return a_string + a_string[-1] + ing
    else: return a_string + ing
    # probably should use regex more

print (present_paticiple('be'))
print (present_paticiple('see'))
print (present_paticiple('lie'))
print (present_paticiple('move'))
print (present_paticiple('hug'))
print (present_paticiple('try'))
print (present_paticiple('fly'))
