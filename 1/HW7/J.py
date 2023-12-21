n, w, l = map(int, input().split())
area = w * l
blocks = []
for block_num in range(n):
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    block_area = abs(x2 - x1) * abs(y2 - y1)
    blocks.append((z1, 1, block_area, block_num+1))
    blocks.append((z2, 0, block_area, block_num+1))

cur_area = 0
current_blocks = 0
min_blocks = n + 1
blocks.sort()
for block in blocks:
    if block[1] == 1:
        cur_area += block[2]
        current_blocks += 1
        if area == cur_area and current_blocks < min_blocks:
            min_blocks = current_blocks
    else:
        cur_area -= block[2]
        current_blocks -= 1

if min_blocks == n + 1:
    print('NO')
else:
    block_set = set()
    for block in blocks:
        if block[1] == 1:
            cur_area += block[2]
            current_blocks += 1
            block_set.add(block[3])
            if area == cur_area and current_blocks == min_blocks:
                print('YES')
                print(min_blocks)
                print(*block_set)
                break
        else:
            cur_area -= block[2]
            current_blocks -= 1
            block_set.remove(block[3])
