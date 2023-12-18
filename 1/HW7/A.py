n, m = map(int, input().split())
teachers = []
for _ in range(m):
    first, last = map(int, input().split())
    teachers.append((first, -1))
    teachers.append((last, 1))
teachers.sort()

parallel = 0
start = None
for x in teachers:
    if parallel == 0:
        start = x[0]
    parallel -= x[1]
    if parallel == 0:
        n -= x[0] - start + 1
print(n)
