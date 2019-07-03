def birthday(n):
	high_numbers = {
		'value': 0,
		'count': 0
	}

	for index in range(len(n)):
		if len(high_numbers) < 1:
			high_numbers['value'] = n[index]
			high_numbers['count'] += 1 
		else:
			if n[index] == high_numbers['value']:
				high_numbers['count'] += 1 
			elif n[index] > high_numbers['value']:
				high_numbers['value'] = n[index]
				high_numbers['count'] = 1
			else:
				continue

	return high_numbers['count']

arr = [3, 2, 1, 3]

print(birthday(arr))