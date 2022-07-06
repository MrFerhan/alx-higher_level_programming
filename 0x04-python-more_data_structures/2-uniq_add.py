#!/usr/bin/python3
def uniq_add(my_list=[]):
    already = []
    uniqsum = 0
    if my_list:
        for i in my_list:
            if i not in already:
                uniqsum += i
                already.append(i)
    return uniqsum
