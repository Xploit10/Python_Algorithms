def staircase(n):
	h = 1
	while h != (n + 1):
		for index in range(n):
			print(' ' * (n-h) + '#' * h)
			h += 1 


n = 6
staircase(n)
