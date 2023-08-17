#!/usr/bin/python3
# AUTHORS Selim

def search_replace(my_list, search, replace):
    if my_list and search and replace:
        return list(map(lambda x: replace if x == search else x, my_list))
    return my_list
