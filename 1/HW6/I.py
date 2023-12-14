n, r, c = map(int, input().split())
heights = [int(input()) for x in range(n)]
heights.sort()


def check(diff):
    i = 0
    teams = 0
    while i < n - c + 1:
        if heights[i + c - 1] - heights[i] <= diff:
            teams += 1
            i += c
        else:
            i += 1
    return teams >= r


left, right = 0, heights[-1] - heights[0]
while right - left != 0:
    mid = (right + left) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1
print(left)
