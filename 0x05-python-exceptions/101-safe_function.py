#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    result = 0
    try:
        result = fct(*args)
        return result
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
