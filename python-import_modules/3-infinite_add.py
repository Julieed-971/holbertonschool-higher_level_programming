#!/usr/bin/python3
import sys

if __name__ == "__main__":
    add = 0
    if len(sys.argv) < 2:
        print("0")
    else:
        for i in range(1, len(sys.argv)):
            add += int(sys.argv[i])
        print("{}".format(add))
