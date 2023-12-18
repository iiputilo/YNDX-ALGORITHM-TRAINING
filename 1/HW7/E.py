events = []
simultaneously_opened = 0
opened_time = 0
n = int(input())

for _ in range(n):
    event = tuple(map(int, input().split()))
    start, end = (event[0] * 60) + event[1], (event[2] * 60) + event[3]
    if start >= end:
        events.append((0, 1))
        events.append((1440, 0))
    events.append((start, 1))
    events.append((end, 0))
events.sort()

for i in range(len(events)):
    if simultaneously_opened == n:
        opened_time += events[i][0] - events[i-1][0]
    if events[i][1] == 1:
        simultaneously_opened += 1
    else:
        simultaneously_opened -= 1
print(opened_time)
