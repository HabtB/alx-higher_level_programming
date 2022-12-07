#!/usr/bin/python3

uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
total = uniq_add(my_list)

print("result: {:d}".format(total))
print(my_list)
