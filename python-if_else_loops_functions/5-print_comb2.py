#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print("{:02d}".format(i))
    elif i >= 0 and i <= 98:
    	print("{:02d}, ".format(i), end='')
