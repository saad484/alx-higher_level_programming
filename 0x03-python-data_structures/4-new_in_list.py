#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    import copy
    cpl = copy.deepcopy(my_list)
    for i in my_list:
        if idx < 0:
            return cpl
        elif idx > len(my_list)-1:
            return cpl
        else:
            cpl[idx] = element
            return cpl
