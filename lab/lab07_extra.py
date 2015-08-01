## Extra Linked List Class and Generic Functions ##

######################
# Linked Lists Class #
######################

class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> len(s)
    4
    >>> s[2]
    3
    >>> s
    Link(1, Link(2, Link(3, Link(4))))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __add__(self, other):
        """Adds two Links, returning a new Link

        >>> Link(1, Link(2)) + Link(3, Link(4, Link(5)))
        Link(1, Link(2, Link(3, Link(4, Link(5)))))
        """
        "*** YOUR CODE HERE ***"
        def new(l):
            if l == Link.empty:
                return l
            else:
                return Link(l.first, new(l.rest))
        if self == Link.empty:
            return new(other)
        elif self.rest == Link.empty:
            return Link(self.first, other)
        return Link(self.first, self.rest+other)

    def __setitem__(self, index, element):
        """Sets the value at the given index to the element

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1] = 5
        >>> s
        Link(1, Link(5, Link(3)))
        >>> s[4] = 5
        Traceback (most recent call last):
        ...
        IndexError
        """
        "*** YOUR CODE HERE ***"
        link = self
        while link != Link.empty and index > 0:
            link, index = link.rest, index-1
        if index == 0:
            link.first = element
        else:
            raise IndexError

def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    if link == Link.empty:
        return []
    else:
        return [link.first] + link_to_list(link.rest)

def reverse(link):
    """Returns a Link that is the reverse of the original.

    >>> Link(1).rest is Link.empty
    True
    >>> link = Link(1, Link(2, Link(3)))
    >>> reverse(link)
    Link(3, Link(2, Link(1)))
    >>> reverse(Link(1))
    Link(1)
    """
    "*** YOUR CODE HERE ***"
    if link == Link.empty:
        return link
    res = Link(link.first)
    while link.rest != Link.empty:
        link = link.rest
        res = Link(link.first, res)
    else:
        return res
    # recursive (and extra for experts)
    # if link.rest is not Link.empty:
    #     second, last = link.rest, link
    #     link = reverse(second)
    #     second.rest, last.rest = last, Link.empty
    # return link


def type_tag(x):
    return type_tag.tags[type(x)]

type_tag.tags = {
    list : 'list',
    Link : 'link'
}

def concat(seq1, seq2):
    """Takes the elements of seq1 and seq2 and adds them together.

    >>> link = Link(4, Link(5, Link(6)))
    >>> lst = [1, 2, 3]
    >>> concat(lst, link)
    [1, 2, 3, 4, 5, 6]
    >>> concat(link, [7, 8])
    Link(4, Link(5, Link(6, Link(7, Link(8)))))
    >>> concat(lst, [7, 8, 9])
    [1, 2, 3, 7, 8, 9]
    """
    if type_tag(seq1) == type_tag(seq2):
        return seq1 + seq2
    else:
        types = (type_tag(seq1), type_tag(seq2))
        if types in concat.adders:
            return concat.adders[types](seq1, seq2)

def add_list_link(lst, link):
    "*** YOUR CODE HERE ***"
    return lst + link_to_list(link)

def add_link_list(link, lst):
    "*** YOUR CODE HERE ***"
    if lst:
        tmp = Link(lst[0])
        l_to_link = tmp
        for i in lst[1:]:
            tmp.rest, tmp = Link(i), tmp.rest
    else:
        l_to_link = Link.empty
    if link:
        return link + l_to_link
    else:
        return l_to_link

concat.adders = {
    ('list', 'link')  : add_list_link,
    ('link', 'list')  : add_link_list
}

from operator import add, sub, mul

def foldl(link, fn, z):
    """ Left fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldl(lst, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl(lst, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl(lst, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    if link is Link.empty:
        return z
    "*** YOUR CODE HERE ***"
    return foldl(link.rest, fn ,fn(z, link.first))

def foldr(link, fn, z):
    """ Right fold
    >>> lst = Link(3, Link(2, Link(1)))
    >>> foldr(lst, sub, 0) # (3 - (2 - (1 - 0)))
    2
    >>> foldr(lst, add, 0) # (3 + (2 + (1 + 0)))
    6
    >>> foldr(lst, mul, 1) # (3 * (2 * (1 * 1)))
    6
    """
    "*** YOUR CODE HERE ***"
    if link is Link.empty:
        return z
    return fn(link.first, foldr(link.rest, fn, z))

identity = lambda x: x

def foldl2(link, fn, z):
    """ Write foldl using foldr
    >>> list = Link(3, Link(2, Link(1)))
    >>> foldl2(list, sub, 0) # (((0 - 3) - 2) - 1)
    -6
    >>> foldl2(list, add, 0) # (((0 + 3) + 2) + 1)
    6
    >>> foldl2(list, mul, 1) # (((1 * 3) * 2) * 1)
    6
    """
    def step(x, g):
        "*** YOUR CODE HERE ***"
        return lambda a: g(fn(a, x))
    return foldr(link, step, identity)(z)

