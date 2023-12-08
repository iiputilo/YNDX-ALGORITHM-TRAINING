n, k = map(int, input().split())
n_seq = list(map(int, input().split()))
n_seq.sort()
k_seq = list(map(int, input().split()))


def bin_search(num, seq):
    l = 0
    r = n - 1
    if num > seq[-1]:
        return seq[-1]
    while r - l != 1:
        m = (l + r) // 2
        if seq[m] < num:
            l = m
        else:
            r = m
    if (num - seq[l]) < (seq[r] - num) or (num - seq[l]) == (seq[r] - num):
        return seq[l]
    else:
        return seq[r]


for i in k_seq:
    print(bin_search(i, n_seq))
