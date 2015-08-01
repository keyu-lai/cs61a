from lab05 import *

## Extra Rooted Trees, Linked Lists, Dictionaries Questions ##

################
# Rooted Trees #
################

# Q5
def height(t):
    """Return the depth of the deepest node in the tree. 

    >>> height(leaf(1))
    0
    >>> height(rooted(1, [leaf(2), leaf(3)]))
    1
    >>> print_tree(t)
    1
      2
      3
        4
        5
      6
        7
    >>> height(t)
    2
    """
    "*** YOUR CODE HERE ***"
    assert is_rooted(t), 'input must be a rooted tree'
    if is_rooted_leaf(t):
        return 0
    else:
        return 1 + max([height(i) for i in branches(t)])

################
# Linked Lists #
################

def linked_list_to_str(lst):
    s = '< '
    while lst != empty:
        if is_link(first(lst)):
            s = s + linked_list_to_str(first(lst)) + ' '
        else:
            s = s + repr(first(lst)) + ' '
        lst = rest(lst)
    return s + '>'

def print_linked_list(lst):
    """
    >>> print_linked_list(empty)
    < >
    >>> print_linked_list(link(1, empty))
    < 1 >
    >>> print_linked_list(link(2, link(3, link(link(4, empty), empty))))
    < 2 3 < 4 > >
    >>> print_linked_list(link(1, link(link(2, link(3, empty)), \
            link(4, link(link(5, link(6, link(7, empty))), empty)))))
    < 1 < 2 3 > 4 < 5 6 7 > >
    """
    print(linked_list_to_str(lst))

# Q6
def link_to_list(linked_lst):
    """Return a list that contains the values inside of linked_lst

    >>> link_to_list(empty)
    []
    >>> lst1 = link(1, link(2, link(3, empty)))
    >>> link_to_list(lst1)
    [1, 2, 3]
    """
    "*** YOUR CODE HERE ***"
    result = []
    while linked_lst != empty:
        result.append(first(linked_lst))
        linked_lst = rest(linked_lst)
    return result

# Q7
def insert_at_end(lst, elem):
    """Return a linked list that is the same as lst with elem added
    at the end.

    >>> lst1 = insert_at_end(empty, 1)
    >>> print_linked_list(lst1)
    < 1 >
    >>> lst2 = insert_at_end(lst1, 2)
    >>> print_linked_list(lst2)
    < 1 2 >
    >>> lst3 = insert_at_end(lst2, 3)
    >>> print_linked_list(lst3)
    < 1 2 3 >
    """
    "*** YOUR CODE HERE ***"
    if lst == empty:
        return link(elem, empty)
    else:
        return link(first(lst), insert_at_end(rest(lst), elem))



################
# Dictionaries #
################

# Q8
def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of
    successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = [word]
        else:
            table[prev].append(word)
        prev = word
    return table

# Q9
def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.
    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        result = result + word + ' '
        word = random.choice(table[word])
    return result + word

# Warning: do NOT try to print the return result of this function
def shakespeare_tokens(path='shakespeare.txt', url='http://goo.gl/SztLfX'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

tokens = shakespeare_tokens()
table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)
