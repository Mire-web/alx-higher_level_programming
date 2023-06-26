#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedList = [item for item in a_dictionary]
    sortedList.sort()
    for keys in sortedList:
        print('{}: {}'.format(keys, a_dictionary.get(keys)))
