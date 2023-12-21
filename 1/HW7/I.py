n, m = map(int, input().split())
events = []
cities = [0] * n
overnight = 0
for i in range(m):
    event = tuple(input().split())
    cities[int(event[0])-1] -= 1
    cities[int(event[2])-1] += 1
    time1, time2 = (int(event[1][:2]) * 60) + int(event[1][3:4]), (int(event[3][:2]) * 60) + int(event[3][3:4])
    if time2 < time1:
        overnight += 1
    events.append((time1, 1, int(event[0])-1))
    events.append((time2, -1, int(event[2])-1))

bad_flag = False
for city in cities:
    if city != 0:
        bad_flag = True
        break
if not bad_flag:
    events.sort()
    buses_in_cities = 0
    for event in events:
        if event[1] == 1:
            if cities[event[2]] > 0:
                cities[event[2]] -= 1
        else:
            cities[event[2]] += 1
    for buses in cities:
        buses_in_cities += buses
    print(buses_in_cities + overnight)
else:
    print(-1)
