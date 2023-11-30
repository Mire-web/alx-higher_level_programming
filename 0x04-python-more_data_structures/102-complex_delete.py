#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    for x in new_dict.keys():
        if a_dictionary.get(x) == value:
            a_dictionary.pop(x)
    return a_dictionary
