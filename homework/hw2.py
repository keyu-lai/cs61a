# CS 61A Fall 2014
# Name:
# Login:

def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

def piecewise(f, g, b):
    """Returns the piecewise function h where:

    h(x) = f(x) if x < b,
           g(x) otherwise

    >>> def negate(x):
    ...     return -x
    >>> abs_value = piecewise(negate, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    "*** YOUR CODE HERE ***"
    def h(x):
        if x < b:
            return f(x)
        else:
            return g(x)
    return h

def intersects(f, x):
    """Returns a function that returns whether f intersects g at x.

    >>> at_three = intersects(square, 3)
    >>> at_three(triple) # triple(3) == square(3)
    True
    >>> at_three(increment)
    False
    >>> at_one = intersects(identity, 1)
    >>> at_one(square)
    True
    >>> at_one(triple)
    False
    """
    "*** YOUR CODE HERE ***"
    def h(g):
        return f(x) == g(x)
    return h

def repeated(f, n):
    """Return the function that computes the nth application of f.

    >>> add_three = repeated(increment, 3)
    >>> add_three(5)
    8
    >>> repeated(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    """
    "*** YOUR CODE HERE ***"
    def h(x):
        k = n
        while k > 0:
            x, k = f(x), k - 1
        return x
    return h

###################
# Church Numerals #
###################

def zero(f):
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(zero(f)(x))

def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"
    return lambda x: f(one(f)(x))

three = successor(two)

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"
    def test(x):
        return x + 1
    return n(test)(0)

def int_to_church(n):
    """This is a Self-defined to Convert a Python integer to Church numeral

    >>> church_to_int(int_to_church(1))
    1
    >>> church_to_int(int_to_church(2))
    2
    >>> church_to_int(int_to_church(3))
    3
    """
    f = zero
    while n > 0:
        f, n = successor(f), n - 1
    return f

def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"
    # return int_to_church(church_to_int(m) + church_to_int(n))
    return lambda f: lambda x: m(f)(n(f)(x))    

def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"
    return lambda f: m(n(f))

def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
    return n(m)


