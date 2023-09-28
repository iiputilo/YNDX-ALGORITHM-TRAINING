a, b, n, m = int(input()), int(input()), int(input()), int(input())


def time(interval, trains_to_cnt):
    min_time = trains_to_cnt + (interval * (trains_to_cnt - 1))
    max_time = trains_to_cnt + (trains_to_cnt * interval) + interval
    return [min_time, max_time]


time1 = time(a, n)
time2 = time(b, m)
if min(time1[1], time2[1]) - max(time1[0], time2[0]) > 0:
    print(max(time2[0], time1[0]), min(time1[1], time2[1]))
elif max(time1[0], time2[0]) - min(time1[1], time2[1]) == 0:
    print(max(time2[0], time1[0]), max(time2[0], time1[0]))
else:
    print(-1)
