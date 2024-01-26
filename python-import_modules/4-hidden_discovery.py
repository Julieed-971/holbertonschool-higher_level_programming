#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for name in dir(hidden_4):
        if not name[0] == '_' and not name[1] == '_':
            print("{}".format(name))
