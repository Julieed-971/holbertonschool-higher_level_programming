#!/usr/bin/python3
'''Function that prints a text with 2 new lines
after each of these characters: ., ? and :
'''


def text_indentation(text):
    '''Function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Parameters
    ----------
    text: str
        text to indent

    Raises
    ------
    TypeError
        If text is not a string

     Returns
    -------
    None
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if len(text) == 0:
        raise TypeError("text_indentation() missing \
            1 required positional argument: 'text'")

    i = 0
    text_list = []
    new_string = ""

    for idx in range(len(text)):
        new_string += text[idx]

        if text[idx] in "?.:":
            text_list.append(new_string)
            new_string = ""

    text_list.append(new_string)
    new_string = ""

    for i in range(len(text_list)):

        if i != len(text_list) - 1:
            print(text_list[i].lstrip() + '\n')

        if i == len(text_list) - 1:
            print(text_list[i].lstrip(), end="")
