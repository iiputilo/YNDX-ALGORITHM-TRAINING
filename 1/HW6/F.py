N, x, y = map(int, input().split())

left = 0
right = (x + y) * N

while (right - left) != 0:
    mid = (right + left) // 2
    if (mid // x) + (mid // y) >= N - 1:
        right = mid
    else:
        left = mid + 1
print(left + min(x, y))
