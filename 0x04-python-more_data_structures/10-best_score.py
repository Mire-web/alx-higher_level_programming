#!/usr/bin/python3
def best_score(a_dictionary):
    biggest_key = ""
    max_value = 0
    if a_dictionary:
        for key in a_dictionary.keys():

            if a_dictionary.get(key) > max_value:
                max_value = a_dictionary.get(key)
                biggest_key = key
        return biggest_key
    else:
        return None
