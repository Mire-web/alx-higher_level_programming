#!/usr/bin/python3
"""
Module: Say_my_name
Desc: a function that formats and prints user name
Author: Mire
"""

def say_my_name(first_name, last_name=""):
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
