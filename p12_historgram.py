# Define a procedure histogram() that takes a list
# of integers and prints a histogram to the
# screen. For example, histogram([4, 9, 7]) should
# print the following:
'''
****
*********
*******
'''


def generate_n_chars(n, c):
    new_string = ""
    for i in range(n): new_string += c
    return new_string

def histogram(int_list):
    for number in int_list:
        print(generate_n_chars(number, '*'))

histogram([4, 9, 7])