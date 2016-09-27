#Sorting


def regular_bubble_sort(lst):
    """returns a sorted list using a basic bubble sort algorithm
        >>> regular_bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


def optimized_bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> optimized_bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    for i in range(len(lst) - 1 ):
        made_swap = False
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                made_swap = True
        if not made_swap:
            break

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    >>> merge_lists([2, 7, 12, 13], [1, 6, 12])
    [1, 2, 6, 7, 12, 12, 13]
    """

    output = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] > list2[0]:
            output.append(list2[0])
            list2 = list2[1:]
        else:
            output.append(list1[0])
            list1 = list1[1:]
    if len(list1) > 0:
        for item in list1:
            output.append(item)
    if len(list2) > 0:
        for item in list2:
            output.append(item)
    return output



##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    if len(lst) < 2:
        return lst
    else:
        list1 = lst[:len(lst)/2]
        list2 = lst[len(lst)/2:]
        return merge_lists(merge_sort(list1), merge_sort(list2))





#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
