#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            if str(type(my_list[i])).__contains__('int'):
                print("{:d}".format(my_list[i]), end='')
                count += 1
    except ValueError:
        pass
    else:
        print()
        return count
