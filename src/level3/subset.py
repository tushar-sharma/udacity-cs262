#!/usr/bin/env python
# Write a procedure that accepts a list as an argument. The procedure should
# print out all of the subsets of that list.

def get_subset(elem , list_set):

    print elem 
    if not list_set:
        return elem

    copy = elem
    elem.append(list_set[0]) 


    get_subset(elem, list_set[1:])

    get_subset(copy, list_set[1:])


def main(list_set):

    get_subset([ ] , list_set)

if __name__=="__main__":
    list_set = ["LM", "ECS", "SBA"]
    main(list_set)
