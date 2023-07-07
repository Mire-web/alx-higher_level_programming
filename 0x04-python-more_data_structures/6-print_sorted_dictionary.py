#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedList = [key for key in a_dictionary.keys()]
    sortedList.sort()
    for keys in sortedList:
        print('{}: {}'.format(keys, a_dictionary.get(keys)))
