#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    if len(argv != 3):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    a = argv[1]
    b = argv[3]
    if argv[2] == '+':
        print('{:d} + {:d} = {:d}'.format(a, b, add(int(a), int(b))))
    elif argv[2] == '-':
        print('{:d} - {:d} = {:d}'.format(a, b, sub(int(a), int(b))))
    elif argv[2] == '*':
        print('{:d} * {:d} = {:d}'.format(a, b, mul(int(a), int(b))))
    elif argv[2] == '/':
        print('{:d} / {:d} = {:d}'.format(a, b, div(int(a), int(b))))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)
