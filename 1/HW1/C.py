new_num = input()
num1, num2, num3 = input(), input(), input()


def std(num):
    number = []
    for char in num:
        try:
            number.append(int(char))
        except Exception:
            continue
    if len(number) == 7:
        final_number = '495' + ''.join(map(str, number))
    elif len(number) == 11:
        final_number = ''.join(map(str, number))[1:]
    else:
        final_number = ''.join(map(str, number))
    return final_number


def comp(num_1, num_2):
    if num_1 == num_2:
        return 'YES'
    else:
        return 'NO'


print(comp(std(new_num), std(num1)))
print(comp(std(new_num), std(num2)))
print(comp(std(new_num), std(num3)))
