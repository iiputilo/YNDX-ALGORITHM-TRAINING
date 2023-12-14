n, a, b, w, h = map(int, input().split())
left = 0
right = min(w, h)
while right - left > 0:
    m = ((right + left) // 2) + 1
    if max((h // (b + (2 * m))) * (w // (a + (2 * m))), (h // (a + (2 * m))) * (w // (b + (2 * m)))) < n:
        right = m - 1
    else:
        left = m
print(right)
