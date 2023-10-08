def max_multiplication(seq):
    positive_list = []
    negative_list = []
    positive = {}
    negative = {}
    for x in seq:
        if len(positive) < 3 or len(negative) < 3:
            if x >= 0:
                if len(positive) != 3:
                    if len(positive_list) < 3:
                        positive_list.append(x)
                        positive_list.sort(reverse=True)
                        if len(positive_list) == 3:
                            positive[0] = positive_list[0]
                            positive[1] = positive_list[1]
                            positive[2] = positive_list[2]
                else:
                    if x >= 0:
                        if x > positive[0]:
                            positive[2] = positive[1]
                            positive[1] = positive[0]
                            positive[0] = x
                        elif positive[0] >= x > positive[1]:
                            positive[2] = positive[1]
                            positive[1] = x
                        elif positive[1] >= x > positive[2]:
                            positive[2] = x
            else:
                if len(negative) != 3:
                    if len(negative_list) < 3:
                        negative_list.append(x)
                        negative_list.sort()
                        if len(negative_list) == 3:
                            negative[0] = negative_list[0]
                            negative[1] = negative_list[1]
                            negative[2] = negative_list[2]
                else:
                    if x < negative[0]:
                        negative[2] = negative[1]
                        negative[1] = negative[0]
                        negative[0] = x
                    elif negative[0] <= x < negative[1]:
                        negative[2] = negative[1]
                        negative[1] = x
                    elif negative[1] <= x < negative[2]:
                        negative[2] = x
        else:
            if x >= 0:
                if x > positive[0]:
                    positive[2] = positive[1]
                    positive[1] = positive[0]
                    positive[0] = x
                elif positive[0] >= x > positive[1]:
                    positive[2] = positive[1]
                    positive[1] = x
                elif positive[1] >= x > positive[2]:
                    positive[2] = x
            else:
                if x < negative[0]:
                    negative[2] = negative[1]
                    negative[1] = negative[0]
                    negative[0] = x
                elif negative[0] <= x < negative[1]:
                    negative[2] = negative[1]
                    negative[1] = x
                elif negative[1] <= x < negative[2]:
                    negative[2] = x
    if len(positive) and len(negative) == 3:
        if positive[0] * positive[1] * positive[2] >= positive[0] * negative[0] * negative[1]:
            return f'{positive[0]} {positive[1]} {positive[2]}'
        else:
            return f'{positive[0]} {negative[0]} {negative[1]}'
    elif len(positive) == 3 and len(negative_list) == 2:
        if positive[0] * positive[1] * positive[2] >= positive[0] * negative_list[0] * negative_list[1]:
            return f'{positive[0]} {positive[1]} {positive[2]}'
        else:
            return f'{positive[0]} {negative_list[0]} {negative_list[1]}'
    elif 1 <= len(positive_list) < 3 and len(negative) == 3:
        return f'{positive_list[0]} {negative[0]} {negative[1]}'
    elif len(positive) == 3 and len(negative_list) < 2:
        return f'{positive[0]} {positive[1]} {positive[2]}'
    elif len(positive_list) == 0:
        seq.sort(reverse=True)
        return ' '.join(map(str, seq[0:3]))
    else:
        if len(positive_list) == 2 and len(negative_list) == 2:
            return f'{positive_list[0]} {negative_list[0]} {negative_list[1]}'
        else:
            return ' '.join(map(str, (positive_list + negative_list)))


print(max_multiplication(list(map(int, input().split()))))
