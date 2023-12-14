n, k = map(int, input().split())
n_seq = list(map(int, input().split()))
n_seq.sort()
k_seq = list(map(int, input().split()))


def left_bin_search(num, seq):
    l = 0
    r = n - 1
    if num > seq[-1]:
        return 'NO'
    while seq[l] < num:
        m = (l + r) // 2
        if seq[m] < num:
            l = m + 1
        else:
            r = m
    if seq[l] == num:
        return 'YES'
    return 'NO'


for i in k_seq:
    print(left_bin_search(i, n_seq))