#!/usr/bin/python3
def safe_print_division(a, b):
    val = None
    try:
        val = a / b
        return val
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(val))
