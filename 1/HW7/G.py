m, n = map(int, input().split())
times = []
for j in range(n):
    helper = tuple(map(int, input().split()))
    for i in range(m):
        times.append([(((i+1) * helper[0]) + ((i // helper[1]) * helper[2])), j])
times.sort()
helpers_count = [0] * n
balloons_count = 0
current_time = 0
total_time = 0
i = 0
while balloons_count < m:
    if current_time != times[i][0]:
        current_time = times[i][0]
        helpers_count[times[i][1]] += 1
        balloons_count += 1
        total_time = current_time
    else:
        helpers_count[times[i][1]] += 1
        balloons_count += 1
    i += 1
print(total_time)
print(*helpers_count)
