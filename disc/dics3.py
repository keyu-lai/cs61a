def is_prime(n):
	from math import sqrt
	def helper(n, m):
		if m > 1:
			if n % m == 0:
				return False
			else:
				return helper(n, m - 1)
		return True
	return helper(n, int(sqrt(n)))

def count_stair_ways(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return count_stair_ways(n - 2) + count_stair_ways(n - 1)

def pascal(row, column):
	if row == column or column == 0:
		return 1
	elif column > row:
		return 0
	else:
		return pascal(row - 1, column - 1) + pascal(row - 1, column)

def has_sum(sum, n1, n2):
	if sum < n1 and sum < n2:
		return False
	elif sum == n1 or sum == n2:
		return True
	else:
		return has_sum(sum - n1, n1, n2) or has_sum(sum - n2, n1, n2)

def has_sum_with_helper(sum, n1, n2):
	def helper(a, b):
		if (a * n1 + b * n2) == sum:
			return True
		elif (a * n1 + b * n2) > sum:
			return False
		else:
			return helper(a + 1, b) or helper(a, b + 1)
	return helper(0, 0)

def sum_range(lower, upper):
	lower1, upper1, lower2, upper2 = 50, 60, 130, 140
	def helper(a, b):
		if ((a * lower1 + b * lower2) >= lower) and ((a * upper1 + b * upper2) <= upper):
			print(a, b)
			return True
		elif (a * upper1 + b * upper2) > upper:
			return False
		else:
			return helper(a + 1, b) or helper(a, b + 1)
	return helper(0, 0)








