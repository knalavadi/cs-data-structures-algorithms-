# --------- #
# Recursion #
# --------- #

# In your own words, what is recursion?

# Recursion is a function calling itself. Think of a set of Russian nesting dolls.  
# When you call a function, you "freeze" where you are until that function returns, and then continue where you left off.

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """
    if not my_list:
        return

    else:
        print my_list[0]
        print_item(my_list[1:])



# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """
    
    print tree.data

    if tree.children:
        for child in tree.children:
            print_all_tree_data(child)




# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """
    if not my_list:
        return 0

    else:
        return 1 + list_length(my_list[1:])


# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
    """

    
    if not tree.children:
        return 1

    count = 1 # count current node
    for child in tree.children:
        count += num_nodes(child)

    return count



#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
