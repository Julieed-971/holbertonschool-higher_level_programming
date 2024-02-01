#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    if my_list_1 is not None and my_list_2 is not None:
        div_list = []
        for i in range(list_length):
            div_result = 0
            try:
                div_result = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
            except TypeError:
                print("wrong type")
            except IndexError:
                print("out of range")
            finally:
                div_list.append(div_result)
        return div_list
