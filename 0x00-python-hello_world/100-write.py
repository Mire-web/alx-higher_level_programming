#!/usr/bin/python3
import os
import sys

data = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
fd = sys.stderr.fileno()
os.write(fd, data.encode())
sys.exit(1)
