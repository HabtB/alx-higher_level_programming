#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = [x for x in my_list]
    for idx, value in enumerate(new):
        if value == search:
            new[idx] = replace
    return new
