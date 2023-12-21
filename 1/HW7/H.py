for _ in range(int(input())):
    current_test = tuple(map(int, input().split()))
    events = []
    num_of_guard = 1
    for x in range(1, len(current_test), 2):
        events.append([current_test[x], 0, num_of_guard])
        events.append([current_test[x + 1], 1, num_of_guard])
        num_of_guard += 1
    events.sort()

    guards_in_op = set()
    good_guards = set()
    all_is_bad = False
    prev_time = -1
    for i in range(len(events)):
        if len(guards_in_op) == 0 and events[i][0] != 0:
            all_is_bad = True
            break
        if prev_time != events[i][0] and len(guards_in_op) == 1:
            good_guards.update(guards_in_op)
        if events[i][1] == 0:
            guards_in_op.add(events[i][2])
        else:
            guards_in_op.remove(events[i][2])
        prev_time = events[i][0]

    if events[-1][0] != 10000:
        all_is_bad = True
    if len(good_guards) != current_test[0] or all_is_bad:
        print('Wrong Answer')
        continue
    print('Accepted')

