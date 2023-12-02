n, k = map(int, input().split())
seq = input()
symbol_in_seq = dict()
left, right, start, length = 0, 0, 0, 0
while right != n:
    if seq[right] not in symbol_in_seq:
        symbol_in_seq[seq[right]] = 1
        right += 1
    elif symbol_in_seq[seq[right]] < k:
        symbol_in_seq[seq[right]] += 1
        right += 1
    else:
        if right - left > length:
            length = right - left
            start = left + 1
        symbol_in_seq[seq[left]] -= 1
        left += 1
if right == n:
    if right - left > length:
        length = right - left
        start = left + 1

print(length, start)
