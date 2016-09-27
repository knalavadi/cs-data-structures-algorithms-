def make_one_sorted_list(lst1, lst2):
    """Merge two sorted lists: ([1,3], [2,4]) => [1,2,3,4]"""

    result_list = []

    while len(lst1) > 0 or len(lst2) > 0:
        if lst1 == []:
            result_list.append(lst2.pop(0))
        elif lst2 == []:
            result_list.append(lst1.pop(0))
        elif lst1[0] < lst2[0]:
            # append and remove first item of lst1
            result_list.append(lst1.pop(0))
        else:
            # append and remove first item of lst2
            result_list.append(lst2.pop(0))

    return result_list