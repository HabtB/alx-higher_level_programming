#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    nlist = []
    for count in range(0, list_length):
        try:
            result = (my_list_1[count] / my_list_2[count])
        except ZeroDivisionError:
            print("division by zero")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            nlist.append(result)
    return nlist
