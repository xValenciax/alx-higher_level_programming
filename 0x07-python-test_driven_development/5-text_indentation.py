#!/usr/bin/python3

"""This Module Defines a text indentation function"""


def trim(text):
    new_text = text
    while new_text[0] == " ":
        new_text = new_text[1:]
    while new_text[-1] == " ":
        new_text = new_text[:-1]
    return new_text


def text_indentation(text):
    """
    a function that prints a text with 2 new line
    after each one of these characters . ? and :
    while handling any errors
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    if text:
        tmp = []
        for ind, ch in enumerate(text):
            tmp.append(ch)
            if ind == len(text) - 1 and len(tmp) > 0:
                print("{}".format(trim(''.join(tmp))), end='')
            elif ch in ['.', '?', ':']:
                print("{}\n".format(trim(''.join(tmp))))
                tmp.clear()
