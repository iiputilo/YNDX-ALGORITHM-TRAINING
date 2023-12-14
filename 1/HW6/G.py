nmt = [int(input()) for x in range(3)]
left = 0
right = nmt[0] // 2

while right - left != 0:
    mid = ((right + left) // 2) + 1
    if (nmt[0] * nmt[1]) - ((nmt[0] - (mid * 2)) * (nmt[1] - (mid * 2))) <= nmt[2]:
        left = mid
    else:
        right = mid - 1
print(right)
