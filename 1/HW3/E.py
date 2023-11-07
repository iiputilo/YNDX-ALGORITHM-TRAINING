buttons = list(map(int, input().split()))
digits = set(int(x) for x in input())

digits_to_add = 0
for k in digits:
    if k not in buttons:
        digits_to_add += 1
print(digits_to_add)
