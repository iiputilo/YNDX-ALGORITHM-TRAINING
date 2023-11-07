union = set()
all = set()
for i in range(int(input())):
    m = int(input())
    a = {input() for j in range(m)}
    all.update(a)
    if i == 0:
        union.update(a)
    else:
        union &= a
print(len(union))
print('\n'.join(union))
print(len(all))
print('\n'.join(all))
