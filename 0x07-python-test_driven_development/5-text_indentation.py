#!/usr/bin/python3
""" A module that prints a text with 2 new lines after
     characters like '.', '?' and ':'.
"""


def text_indentation(text):
    """ A function that prints a text with two new lines
    after characters: ". ? :"
    Args:
        text: a string characters
    """

    if type(text) is not str:
        raise TypeError('text must be a string')
    nstr = text.replace(".", ".\n\n")
    nstr2 = nstr.replace("?", "?\n\n")
    nstr3 = nstr2.replace(":", ":\n\n")
    nstr4 = nstr3.strip(" ")
    nstr5 = nstr4.split("\n")
    for i in range(len(nstr5)):
        nstr5[i] = nstr5[i].strip(" ")
    print("\n".join(nstr5), end="")
