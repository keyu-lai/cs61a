def partition(n, m):
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m == 0:
		return 0
	i = n // m
	sum = 0
	while i > 0:
		sum, i = sum + partition(n - m * i, m - 1), i - 1
	sum += partition(n, m - 1) 

	return sum

def count_partitions(n, m):
	if n == 0:
		return 1
	elif n < 0:
		return 0
	elif m == 0:
		return 0
	else:
		return count_partitions(n-m, m) + count_partitions(n, m-1)
