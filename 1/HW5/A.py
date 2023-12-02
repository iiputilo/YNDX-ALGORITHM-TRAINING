num_of_tshirts = int(input())
tshirts_colors = list(map(int, input().split()))
num_of_trousers = int(input())
trousers_colors = list(map(int, input().split()))


def min_diff(colors1, colors2, num1, num2):
    if num1 == num2 == 1:
        return f'{colors1[0]} {colors2[0]}'
    min_difference, color1, color2 = abs(colors1[0] - colors2[0]), colors1[0], colors2[0]
    i, j = 0, 0
    while i != num1 and j != num2:
        if abs(colors1[i] - colors2[j]) == 0:
            return f'{colors1[i]} {colors2[j]}'
        if abs(colors1[i] - colors2[j]) < min_difference:
            min_difference, color1, color2 = abs(colors1[i] - colors2[j]), colors1[i], colors2[j]
        if colors1[i] < colors2[j]:
            i += 1
        else:
            j += 1
    return f'{color1} {color2}'


print(min_diff(tshirts_colors, trousers_colors, num_of_tshirts, num_of_trousers))
