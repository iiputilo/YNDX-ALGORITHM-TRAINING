n, r = map(int, input().split())
monuments = list(map(int, input().split()))

left = 0
right = 1
ans = 0
while right != n:
    if monuments[right] - monuments[left] > r:
        ans += n - right
        left += 1
        right -= 1
    right += 1
print(ans)
