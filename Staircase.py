

def staircase(n):
	complete = False
	while complete != True:
		h = 1
		for index in range(n):
			print(' ' * (n-h) +'#' * h)
			h += 1 
		complete = True

n = 6
staircase(n)


