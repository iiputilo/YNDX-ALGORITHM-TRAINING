a, b, c = int(input()), int(input()), int(input())

if c < 0 or (a == 0 and b ** 0.5 != c):
    print('NO SOLUTION')
elif a == 0 and (b ** 0.5) == c:
    print('MANY SOLUTIONS')
else:
    sol = (c ** 2 - b) / a
    if sol == int(sol):
        print(int(sol))
    else:
        print('NO SOLUTION')
