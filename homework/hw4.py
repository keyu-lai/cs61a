# CS 61A Fall 2014
# Name:
# Login:

def interval(a, b):
    """Construct an interval from a to b."""
    "*** YOUR CODE HERE ***"
    return [a, b] if a < b else [b, a]

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    """
    "*** YOUR CODE HERE ***"
    assert lower_bound(y)*upper_bound(y) > 0, 'the divisor interval cannot cross zero'
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    "*** YOUR CODE HERE ***"
    return interval(lower_bound(x) - upper_bound(y), upper_bound(x) - lower_bound(y))

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

# These two intervals give different results for parallel resistors:
"*** YOUR CODE HERE ***"
par1(interval(1,2), interval(3,4))
par2(interval(1,2), interval(3,4))


def multiple_references_explanation():
    return """The mulitple reference problem..."""


def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    def f(x):
        return a*x*x + b*x +c
    if a == 0:
        return interval(f(lower_bound(x)), f(upper_bound(x))) if b > 0 else interval(f(upper_bound(x)), f(lower_bound(x)))
    else:
        extreme = -b/(2*a)
        if lower_bound(x) < extreme < upper_bound(x):
            return interval(min(f(lower_bound(x)), f(upper_bound(x)), f(extreme)), max(f(lower_bound(x)), f(upper_bound(x)), f(extreme)))
        else:
            return interval(min(f(lower_bound(x)), f(upper_bound(x))), max(f(lower_bound(x)), f(upper_bound(x))))

def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"

    # Newton's method
    def improve(update, close, guess=1, max_updates=100):
        """Iteratively improve guess with update until close(guess) is true or
        max_updates have been applied."""
        k = 0
        while not close(guess) and k < max_updates:
            guess = update(guess)
            k = k + 1
        return guess

    def approx_eq(x, y, tolerance=1e-15):
        return abs(x - y) < tolerance

    def find_zero(f, df, guess):
        """Return a zero of the function f with derivative df."""
        def near_zero(x):
            return approx_eq(f(x), 0)
        return improve(newton_update(f, df), near_zero, guess)

    def newton_update(f, df):
        """Return an update function for f with derivative df,
        using Newton's method."""
        def update(x):
            return x - f(x) / df(x)
        return update

    from math import pow
    def f(x):
        result = 0
        for i in range(0, len(c)):
            result += c[i]*pow(x, i)
        return result

    def df(x):
        result = 0
        for i in range(1, len(c)):
            result += i*c[i]*pow(x, i-1)
        return result

    def ddf(x):
        result = 0
        for i in range(2, len(c)):
            result += i*(i-1)*c[i]*pow(x, i-2)
        return result
        
    def find_poly_zero(guess):
        return find_zero(df, ddf, guess)

    step = (upper_bound(x)-lower_bound(x))/len(c)
    init_set = [lower_bound(x)]
    for i in range(1, len(c)+1):
        init_set.append(init_set[i-1] + step)
    zero_set = set([find_poly_zero(i) for i in init_set])
    extreme_set = [f(i) for i in zero_set if lower_bound(x) < i < upper_bound(x)]
    extreme_set = extreme_set + [f(lower_bound(x)), f(upper_bound(x))]
    return interval(min(extreme_set), max(extreme_set))









