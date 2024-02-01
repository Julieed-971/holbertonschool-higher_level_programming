#!/usr/bin/python3

def safe_print_division(a, b):
    div_result = 0
    try:
        div_result = a / b
    except ZeroDivisionError:
        div_result = None
        return None
    finally:
        print("Inside result: {}".format(div_result))
        return div_result
