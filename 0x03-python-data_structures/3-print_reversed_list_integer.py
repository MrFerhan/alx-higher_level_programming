#!/usr/bin/python3
# def fun that prnt all int of a list, in revers
def print_reversed_list_integer(my_list=[]):
#change my list to reversed
    my_list.reverse()

#create for loop to print an int per line and use strformat to print int
    for i in my_list:
        print("{:d}".format(i))
