#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0
    roman_figs = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1}
    prev_int = 4000
    total = 0
    x = 0
    for x in roman_string:
        for i in roman_figs.keys():
            if x == i:
                if prev_int < roman_figs.get(i):
                    total -= prev_int
                    prev_int = roman_figs.get(i) - prev_int
                else:
                    prev_int = roman_figs.get(i)
                total += prev_int
    return total
