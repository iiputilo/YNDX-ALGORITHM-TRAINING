n, m = map(int, input().split())
events = []
for _ in range(n):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    events.append((x, -1))
    events.append((y, 1))
dots = tuple(map(int, input().split()))
dots_dict = dict()
for dot in dots:
    events.append((dot, 0))
events.sort()

parallel = 0
for i in range(len(events)):
    if events[i][1] != 0:
        parallel -= events[i][1]
    else:
        dots_dict[events[i][0]] = parallel

to_print = [dots_dict[j] for j in dots]
print(*to_print)
