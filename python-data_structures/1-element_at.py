#!/usr/bin/python3

def element_at(my_list, idx):
    for i in range(len(my_list)):
        if idx < 0:
            return None
        elif idx > len(my_list):
            return None
        elif i == idx:
            return my_list[i]
