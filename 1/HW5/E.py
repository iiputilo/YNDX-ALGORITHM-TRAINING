num_of_trees, num_of_trees_sorts = map(int, input().split())
trees_sorts = list(map(int, input().split()))
active_sorts = dict()
min_left, min_right = 0, num_of_trees - 1
left, right, buffer = 0, 0, 0
flag1, flag2 = True, True
while True:
    while len(active_sorts) != num_of_trees_sorts:
        if trees_sorts[right] not in active_sorts:
            active_sorts[trees_sorts[right]] = 1
        else:
            active_sorts[trees_sorts[right]] += 1
        right += 1
    while flag1:
        if active_sorts[trees_sorts[left]] - 1 != 0:
            active_sorts[trees_sorts[left]] -= 1
            left += 1
        else:
            if right - left - 1 < min_right - min_left:
                min_right = right - 1
                min_left = left
            buffer = trees_sorts[left]
            active_sorts[buffer] -= 1
            left += 1
            flag1, flag2 = False, True
    if min_right - min_left == num_of_trees_sorts - 1:
        break
    if right == num_of_trees:
        break
    while flag2:
        active_sorts[trees_sorts[right]] += 1
        right += 1
        if active_sorts[buffer] == 1:
            flag1, flag2 = True, False
            break
        if right == num_of_trees:
            break
print(min_left + 1, min_right + 1)
