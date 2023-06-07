#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i >= 97 and i <= 122):
        if i % 2 == 0:
            odd = 0
        else:
            odd = 32
        print('{}'.format(chr(i - odd)), end="")
