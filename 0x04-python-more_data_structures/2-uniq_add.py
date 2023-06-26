#!/usr/bin/python3
def uniq_add(my_list):
    uniq_set = set()
    result = 0
    for x in my_list:
        uniq_set.add(x)
    for x in uniq_set:
        result += x
    return result
