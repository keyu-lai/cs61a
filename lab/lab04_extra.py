from lab04 import *

# Q5
def reverse_iter(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    assert type(lst) == list, "lst must be a list"
    re = []
    for item in lst:
        re = [item] + re
    return re

def reverse_recursive(lst):
    """Returns the reverse of the given list.

    >>> reverse_recursive([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    assert type(lst) == list, "lst must be a list"
    if len(lst) < 2:
        return lst
    return (reverse_recursive(lst[1:]) + [lst[0]])

# Q8
def mergesort(seq):
    """Mergesort algorithm.

    >>> mergesort([4, 2, 5, 2, 1])
    [1, 2, 2, 4, 5]
    >>> mergesort([])     # sorting an empty list
    []
    >>> mergesort([1])   # sorting a one-element list
    [1]
    """
    "*** YOUR CODE HERE ***"
    #iterative
    # if not seq:
    #     return []
    # queue = [[elem] for elem in seq]
    # while len(queue) > 1:
    #     first, second = queue[0], queue[1]
    #     queue = queue[2:] + [merge(first, second)]
    # return queue[0]

    # recursive
    assert type(seq) == list
    if len(seq) < 2:
        return seq
    middle = len(seq) // 2
    return merge(mergesort(seq[:middle]), mergesort(seq[middle:]))

# Q12
def add_matrices(x, y):
    """
    >>> add_matrices([[1, 3], [2, 0]], [[-3, 0], [1, 2]])
    [[-2, 3], [3, 2]]
    """
    "*** YOUR CODE HERE ***"
    return [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
