s11, s12, s21, s22 = map(int, input().split())
areas = {}

if s22 >= s12:
    areas[(s21 + s11) * s22] = f'{s21 + s11} {s22}'
else:
    areas[(s21 + s11) * s12] = f'{s21 + s11} {s12}'

if s11 >= s21:
    areas[(s12 + s22) * s11] = f'{s12 + s22} {s11}'
else:
    areas[(s12 + s22) * s21] = f'{s12 + s22} {s21}'

if s12 >= s21:
    areas[(s22 + s11) * s12] = f'{s22 + s11} {s12}'
else:
    areas[(s22 + s11) * s21] = f'{s22 + s11} {s21}'

if s11 >= s22:
    areas[(s12 + s21) * s11] = f'{s12 + s21} {s11}'
else:
    areas[(s12 + s21) * s22] = f'{s12 + s21} {s22}'

print(areas[min(areas)])
