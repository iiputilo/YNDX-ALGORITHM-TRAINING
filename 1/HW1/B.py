a = int(input())
b = int(input())
c = int(input())

if ((a + b) > c) & ((a + c) > b) & ((b + c) > a):
    print('YES')
else:
    print('NO')
