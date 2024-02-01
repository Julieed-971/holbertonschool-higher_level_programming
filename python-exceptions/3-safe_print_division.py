#!/usr/bin/python3

def safe_print_division(a, b):
    div_result = 0
    try:
        div_result = a / b
        return div_result
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {:.1f}".format(div_result))
