
def gradeCheck(grades):
	final_grades = []

	for index in range(len(grades)):
		if grades[index] < 38:
			final_grades.append(grades[index])
		else:
			check = (40 - grades[index]) % 5
			if check < 3:
				print(grades[index] + check)
				final_grades.append(grades[index] + check)
			elif check == 3 or check > 3:
				final_grades.append(grades[index])

	return final_grades


n = [33, 73, 38, 67]
print(gradeCheck(n))