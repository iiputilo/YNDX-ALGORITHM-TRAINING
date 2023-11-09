n = int(input())
x_set = set()
y_max = dict()
for _ in range(n):
    params = list(map(int, input().split()))
    x_set.add(params[0])
    try:
        y_max[params[0]] = max(y_max[params[0]], params[1])
    except KeyError:
        y_max[params[0]] = params[1]
x_set = sorted(x_set)
max_height = 0
for x in x_set:
    max_height += y_max[x]
print(max_height)
