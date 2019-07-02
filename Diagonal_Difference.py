def diagonalDifference(arr):
    left_total = 0
    left_index = 0 

    right_total = 0
    right_index = len(arr) - 1

    for row in range(len(arr)):
        right = arr[row][right_index]
        right_index -= 1
        right_total += right

        left = arr[row][left_index]
        left_index += 1
        left_total += left

    if right_total > left_total:
        result = right_total - left_total
    else:
        result = left_total - right_total

    return result



input = ([[-1, 1, -7, -8], [-10, -8, -5, -2], [0, 9, 7, -1], [4,4,-2,1]])

print(diagonalDifference(input))