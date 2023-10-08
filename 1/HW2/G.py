def max_multiplication(seq):
    positive = [0, 0]
    negative = [0, 0]
    for x in seq:
        if x > positive[0]:
            positive[1] = positive[0]
            positive[0] = x
        elif positive[0] >= x > positive[1]:
            positive[1] = x
        if x < negative[0]:
            negative[1] = negative[0]
            negative[0] = x
        elif negative[0] <= x < negative[1]:
            negative[1] = x
    if len(seq) == 2:
        return f'{" ".join(map(str, list(sorted(seq))))}'
    if positive[0] * positive[1] >= negative[0] * negative[1]:
        positive.sort()
        return f'{positive[0]} {positive[1]}'
    else:
        negative.sort()
        return f'{negative[0]} {negative[1]}'


print(max_multiplication(list(map(int, input().split()))))
