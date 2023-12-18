lives = []
cnt = 1
for _ in range(int(input())):
    life = tuple(map(int, input().split()))
    if not (life[2] + 18 > life[5] or (life[2] + 18 == life[5] and life[1] > life[4]) or
            (life[2] + 18 == life[5] and life[1] == life[4] and life[0] > life[3])):
        if ((life[5] - life[2] > 80) or (life[5] - life[2] == 80 and life[4] > life[1]) or
                (life[5] - life[2] == 80 and life[1] == life[4] and life[3] > life[0])):
            lives.append((life[2] + 18, life[1], life[0], 1, cnt))
            lives.append((life[2] + 80, life[1], life[0], 0, cnt))
        else:
            lives.append((life[2] + 18, life[1], life[0], 1, cnt))
            lives.append((life[5], life[4], life[3], 0, cnt))
    cnt += 1
lives.sort()

sets = []
current_set = []
flag = False
for i in range(len(lives)):
    if lives[i][3] == 1:
        current_set.append(lives[i][4])
        flag = False
    else:
        if not flag:
            sets.append(sorted(current_set))
            current_set.remove(lives[i][4])
            flag = True
        else:
            current_set.remove(lives[i][4])

if len(sets) > 0:
    for j in sets:
        print(*j)
else:
    print(0)
