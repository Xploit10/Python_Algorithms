def function(arr):
	""" 
	Not the best time complexity. 
	Can implement as O(n)
	"""
	# SORT O(n^2)
	for index in range(len(arr)):
		currentvalue = arr[index]
		position = index

		while position > 0 and arr[position - 1] > currentvalue:
			arr[position] = arr[position - 1]
			position = position - 1

		arr[position] = currentvalue

	# MAX NUMBER
	max_values = arr[1:]
	max_total = 0
	# MIN NUMBER
	min_values = arr[:-1]
	min_total = 0

	for index in range(len(arr) - 1):
		max_total += max_values[index]
		min_total += min_values[index]

	return [min_total, max_total]


arr = [7, 69, 2, 221, 8974]

print(function(arr))