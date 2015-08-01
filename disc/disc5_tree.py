def foo(lst):
	return [x*i for i, x in enumerate(lst) if i%2 == 0]

def is_leaf(tree):
	return type(tree) != list

def height(tree):
	if is_leaf(tree):
		return 0
	else:
		return max([height(x) for x in tree]) + 1

def join(tree):
	if type(tree) == str:
		return tree
	else:
		result = ''
		for i in tree:
			result = result + join(i)
		return result

def search(tree, x):
	"""Returns the minimum depth of a leaf with value X in
	TREE, False if not found.
	>>> search([2, [3, 4], [1, [5, [3]]]], 3)
	2
	>>> search([2, [3, 4], [1, [5, [3]]]], 6)
	False
	"""
	def search(tree, x, d):
		if type(tree) != list:
			return d if tree == x else float('inf')
		else:
			return min([search(i, x, d+1) for i in tree])

	tmp = search(tree, x, 0) 
	return False if tmp == float('inf') else tmp

def rooted(value, branches):
	return [value] + list(branches)

def root(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def leaf(value):
	return rooted(value, [])

def is_rooted_leaf(tree):
	return branches(tree) == []

def reduce(fn, s, init):
	reduced = init
	for x in s:
		reduced = fn(reduced, x)
	return reduced

def apply_to_all(fn, s):
	return [fn(x) for x in s]

from operator import add, mul
def eval_tree(tree):
	"""Evaluates an expression tree with functions as root
	>>> eval_tree(leaf(1))
	1
	>>> expr = rooted(mul, [leaf(2), leaf(3)])
	>>> eval_tree(expr)
	6
	>>> eval_tree(rooted(add, [expr, leaf(4)]))
	10
	"""
	if is_rooted_leaf(tree):
		return root(tree)
	else:		
		init = 1 if root(tree) == mul else 0
		return reduce(root(tree), apply_to_all(eval_tree, branches(tree)), init)

def hailstone_tree(n, h):
	"""Generates a rooted tree of hailstone numbers that
	will reach N, with height H.
	>>> hailstone_tree(1, 0)
	[1]
	>>> hailstone_tree(1, 4)
	[1, [2, [4, [8, [16]]]]]
	>>> hailstone_tree(8, 3)
	[8, [16, [32, [64]], [5, [10]]]]
	"""
	if h == 0:
		return [n]
	else:
		if (n-1)%3 == 0 and (n-1)//3 > 1:
			return rooted(n, [hailstone_tree(2*n, h-1), hailstone_tree((n-1)//3, h-1)])
		else:
			return rooted(n, [hailstone_tree(2*n, h-1)])

def find_path(tree, x):
	""" Returns a path in a tree to a leaf with value X,
	False if such a leaf is not present.
	>>> r, l = rooted, leaf
	>>> t = r(2, [r(7, [l(3), r(6, [r(5, [l(9)]), l(11)])]), l(15)])
	>>> find_path(t, 5)
	[2, 7, 6, 5]
	>>> find_path(t, 6)
	[2, 7, 6]
	>>> find_path(t, 10)
	False
	"""
	if root(tree) == x:
		return [root(tree)]
	elif is_rooted_leaf(tree):
		return False
	else:
		for i in branches(tree):
			tmp = find_path(i, x)
			if not (type(tmp) == bool):
				return [root(tree)] + tmp
		return False












