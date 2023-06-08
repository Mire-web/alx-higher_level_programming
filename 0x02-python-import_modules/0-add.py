#!/usr/bin/python3
if __name__ = "__main__":
    a = 1
    b = 2
    add_num = __import__("add_0")
    print('{:d} + {:d} = {:d}'.format(a, b, add_num.add(a, b)))
