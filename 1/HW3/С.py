n, m = input().split()
ann = set()
boris = set()
for _ in range(int(n)):
    ann.add(int(input()))
for _ in range(int(m)):
    boris.add(int(input()))

print(len(ann & boris))
print(*sorted(ann & boris))
print(len(ann - boris))
print(*sorted(ann - boris))
print(len(boris - ann))
print(*sorted(boris - ann))
