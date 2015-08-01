def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

# Q6
def deep_len(lst):
    """Returns the deep length of the list.

    >>> deep_len([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # deep list
    >>> deep_len(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> deep_len(x)
    6
    """
    "*** YOUR CODE HERE ***"
    if type(lst) != list:
        return 1
    elif not lst:
        return 0
    sum = 0
    for i in lst:
        sum += deep_len(i)
    return sum

# Q7
def merge(lst1, lst2):
    """Merges two sorted lists recursively.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    # recursive
    # if not lst1 or not lst2:
    #     return lst1 + lst2
    # elif lst1[0] < lst2[0]:
    #     return [lst1[0]] + merge(lst1[1:], lst2)
    # else:
    #     return [lst2[0]] + merge(lst1, lst2[1:])

    # Iterative solution 
    new = []
    while lst1 and lst2:
        if lst1[0] < lst2[0]:
            new += [lst1[0]]
            lst1 = lst1[1:]
        else:
            new += [lst2[0]]
            lst2 = lst2[1:]
    if lst1:
        return new + lst1
    else:
        return new + lst2


# Q11
def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """ 
    "*** YOUR CODE HERE ***"
    return [[x, fn(x)] for x in seq if fn(x) >= lower and fn(x) <= upper]

# Q13
def deck():
    "*** YOUR CODE HERE ***"
    [[suit, value] for suit in ['spades', 'clubs', 'diamonds', 'hearts'] for value in range(1, 14)]

def sort_deck(deck):
    "*** YOUR CODE HERE ***"

