#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    nlist = []
    for count in range(list_length):
        result = 0
        try:
            result = (my_list_1[count] / my_list_2[count])
        except ZeroDivisionError:
            result = 0
            print("division by zero")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            nlist.append(result)
    return nlist
