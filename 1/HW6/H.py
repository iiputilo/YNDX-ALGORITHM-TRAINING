n, k = map(int, input().split())
l = [int(input()) for x in range(n)]

left = 0
right = 10000000
while right - left != 0:
    mid = (right + left) // 2 + 1
    summ = 0
    for i in l:
        summ += i // mid
    if summ >= k:
        left = mid
    else:
        right = mid - 1
print(right)
