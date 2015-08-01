# CS 61A Fall 2014
# Name:
# Login:


def two_equal(a, b, c):
    """Return whether exactly two of the arguments are equal and the
    third is not.

    >>> two_equal(1, 2, 3)
    False
    >>> two_equal(1, 2, 1)
    True
    >>> two_equal(1, 1, 1)
    False
    >>> result = two_equal(5, -1, -1) # return, don't print
    >>> result
    True

    """
    "*** YOUR CODE HERE ***"
    if (a == b) and (a != c):
        return True
    if (a == c) and (a != b):
        return True
    if (b == c) and (b != a):
        return True
    return False

def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    assert (a > 0) and (b > 0), "a and b must be integer"
    def hailstone(n, find):
        if n == find:
            return True
        while n != 1:
            if(n % 2 == 0):
                n = n // 2
            else:
                n = 3 * n + 1
            if n == find:
                return True
        return False
    return hailstone(a, b) or hailstone(b, a)


def near_golden(perimeter):
    """Return the integer height of a near-golden rectangle with PERIMETER.

    >>> near_golden(42) # 8 x 13 rectangle has perimeter 42
    8
    >>> near_golden(68) # 13 x 21 rectangle has perimeter 68
    13
    >>> result = near_golden(100) # return, don't print
    >>> result
    19

    """
    "*** YOUR CODE HERE ***"
    assert type(perimeter) == int, "Perimeter must be an integer"
    assert perimeter % 2 == 0, "Perimeter must be even"
    assert perimeter > 3, "Perimeter must be greater than 3"

    def cal(h):
        w = perimeter / 2 - h
        return abs(h / w - w / h + 1)

    from math import sqrt
    h = int((3 - sqrt(5)) * perimeter / 4)

    if cal(h) <= cal(h + 1):
        return h
    else:
        return h + 1




