#!/usr/bin/env python
# Write a procedure that accepts a list as an argument. The procedure should
# print out all of the subsets of that list.

def get_subset(elem , list_set):

    if not list_set:
        return elem
    else:
        print elem
	current_elem = elem 
	#insert the first element of the list 
	elem.append(list_set[0]) 

        # get the left tree for elem in the list
        get_subset(elem, list_set[1:])

        # get the right tree for elem not in the list
        get_subset(current_elem, list_set[1:])


def main(list_set):

    get_subset([ ] , list_set)

if __name__=="__main__":
    list_set = ["LM", "ECS", "SBA"]
    main(list_set)
