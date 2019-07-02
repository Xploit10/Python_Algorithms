def compareTriplets(a, b):
    alice = 0
    bob = 0
    
    for index in range(len(a)):
        if a[index] > b[index]:
            alice += 1 
        elif a[index] < b[index]:
            bob += 1 
        else:
            continue 
    return [alice, bob]

a = [5, 6, 7]
b = [3, 6 ,10]

print(compareTriplets(a, b))