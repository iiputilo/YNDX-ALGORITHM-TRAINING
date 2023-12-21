import sys

sys.setrecursionlimit(100000)
n = int(input())
family_tree = [[None, []] for _ in range(n)]
i = 0
people_added = 1
while people_added != n:
    child, parent = map(str, input().split())
    people_added += 1
    j = 0
    flag_parent, flag_child = False, False
    child_index, parent_index = 0, 0
    while family_tree[j][0] is not None and j != n - 1:
        if family_tree[j][0] == parent:
            flag_parent = True
            if flag_child:
                family_tree[j][1].append(child_index)
                break
            else:
                parent_index = j
        if family_tree[j][0] == child:
            flag_child = True
            if flag_parent:
                family_tree[parent_index][1].append(j)
                break
            child_index = j
        j += 1
    if flag_child and flag_parent:
        continue
    elif flag_child and not flag_parent:
        family_tree[i][0] = parent
        family_tree[i][1].append(child_index)
    elif flag_parent:
        family_tree[i][0] = child
        family_tree[parent_index][1].append(i)
    else:
        family_tree[i][0] = parent
        family_tree[i][1].append(i + 1)
        family_tree[i + 1][0] = child
        i += 1
    i += 1

counter = -1


def children_count(anc_index):
    global counter
    for son in family_tree[anc_index][1]:
        children_count(son)
        counter += 1
    if family_tree[anc_index][1] == 0:
        raise TypeError


parents = []
for i in range(n):
    counter = -1
    try:
        children_count(i)
    except Warning:
        parents.append((family_tree[i][0], counter))
parents.sort()
for parent in parents:
    print(f'{parent[0]} {parent[1]}')
