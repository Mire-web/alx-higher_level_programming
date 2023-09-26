#!/usr/bin/python3
"""
Module: Text Indentation
Desc: Adds two new lines after (.), (?) and (:)
Author: Mire
"""

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        indented_text = text.replace(". ", ".\n\n").replace("? ", "?\n\n").replace(": ", ":\n\n")
        print(indented_text, end="")
