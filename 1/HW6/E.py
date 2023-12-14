abc = [int(input()) for x in range(3)]
left = 0
right = (abc[0] + abc[1] + abc[2]) * 3

while right - left != 0:
    mid = (right + left) // 2
    if ((abc[0] * 2) + (abc[1] * 3) + (abc[2] * 4) + (mid * 5)) * 2 >= (abc[0] + abc[1] + abc[2] + mid) * 7:
        right = mid
    else:
        left = mid + 1
print(left)
