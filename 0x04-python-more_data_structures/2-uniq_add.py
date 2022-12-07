#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    total = 0
    for ints in my_list:
        if ints not in new_list:
            new_list.append(ints)
            total += ints
    return total
