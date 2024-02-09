#!/usr/bin/python3
'''Function that write the first and last name'''


def say_my_name(first_name, last_name=""):
    '''
    Function that prints "My name is" and the first and or last name

    Parameters
    ----------
    first_name: string
        string for a name
    last_name: string
        string for a name

    Raises
    ------
    TypeError
        If first_name or last_name are not strings

    Returns
    -------
    None
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
