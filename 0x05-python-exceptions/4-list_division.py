#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.
    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    nlist = []
    for count in range(0, list_length):
        try:
            result = (my_list_1[count] / my_list_2[count])
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by zero")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            nlist.append(result)
    return nlist
