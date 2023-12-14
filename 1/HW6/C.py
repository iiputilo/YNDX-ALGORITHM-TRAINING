w, h, n = map(int, input().split())
left = round((w * h * n) ** 0.5)
right = left * 2

while right - left > 0:
    middle = (left + right) // 2
    if (middle // w) * (middle // h) >= n:
        right = middle
    else:
        left = middle + 1
print(left)
