a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())

max_side, min_side = max(d, e), min(d, e)
var1_min_side, var1_max_side = min(a, b), max(a, b)
var2_min_side, var2_max_side = min(a, c), max(a, c)
var3_min_side, var3_max_side = min(c, b), max(c, b)

if (var1_min_side <= min_side and var1_max_side <= max_side) or (var2_min_side <= min_side and var2_max_side <= max_side) or (var3_min_side <= min_side and var3_max_side <= max_side):
    print('YES')
else:
    print('NO')
