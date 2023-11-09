num_of_keys = int(input())
key_durability = list(map(int, input().split()))
_ = input()
pressed_keys = list(map(int, input().split()))
presses = [0] * num_of_keys
for x in pressed_keys:
    presses[x-1] += 1
for y in range(num_of_keys):
    if key_durability[y] < presses[y]:
        print('YES')
    else:
        print('NO')
