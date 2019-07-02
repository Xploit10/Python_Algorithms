def plusMinus(arr):
    positive = {
        'total': 0,
        'count': 0,
        'ratio': 0
    }
    zero = {
        'total': 0,
        'count': 0,
        'ratio': 0
    }
    negative = {
        'total': 0,
        'count': 0,
        'ratio': 0
    }
    ratio = len(arr)
    
    for index in range(ratio):
        if arr[index] > 0:
            positive['total'] += arr[index]
            positive['count'] += 1 
        elif arr[index] == 0:
            zero['total'] += arr[index]
            zero['count'] += 1
        else:
            negative['total'] += arr[index]
            negative['count'] += 1
    positive['ratio'] = (1 / ratio) * positive['count']
    zero['ratio'] = (1 / ratio) * zero['count']
    negative['ratio'] = (1 / ratio) * negative['count']

    print("%.5f" % positive['ratio'])
    print("%.5f" % negative['ratio'])
    print("%.5f" % zero['ratio'])

input = [-4, 3, -9, 0, 4, 1]

plusMinus(input)