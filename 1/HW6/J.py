n, l = map(int, input().split())
seqs = [list(map(int, input().split())) for _ in range(n)]


def median(seq1, seq2):
    last = None
    i, j = 0, 0
    for _ in range(l):
        if i < l and (j == l or seq1[i] < seq2[j]):
            last = seq1[i]
            i += 1
        else:
            last = seq2[j]
            j += 1
    return last


for x in range(n - 1):
    for y in range(x + 1, n):
        print(median(seqs[x], seqs[y]))
