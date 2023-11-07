a, b = set(map(int, input().split())), set(map(int, input().split()))
print(*sorted(list(_ for _ in a if _ in b)))

