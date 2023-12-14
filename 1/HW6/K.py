n, length = map(int, input().split())
seq_params = [list(map(int, input().split())) for _ in range(n)]
seqs = [seq_params[x][0:1] for x in range(n)]
seqs_d = [seq_params[y][1:2] for y in range(n)]


def median(seq1, seq2):
    last = None
    marker1 = marker2 = 0
    for _ in range(length):
        if len(seqs[seq1]) == marker1:
            seqs[seq1].append(0)
            seqs_d[seq1].append(0)
            seqs_d[seq1][marker1] = ((seq_params[seq1][2] * seqs_d[seq1][marker1-1]) + seq_params[seq1][3]) % seq_params[seq1][4]
            seqs[seq1][marker1] = seqs[seq1][marker1-1] + seqs_d[seq1][marker1-1]
        if len(seqs[seq2]) == marker2:
            seqs[seq2].append(0)
            seqs_d[seq2].append(0)
            seqs_d[seq2][marker2] = ((seq_params[seq2][2] * seqs_d[seq2][marker2-1]) + seq_params[seq2][3]) % seq_params[seq2][4]
            seqs[seq2][marker2] = seqs[seq2][marker2-1] + seqs_d[seq2][marker2-1]
        if marker1 < length and (marker2 == length or seqs[seq1][marker1] < seqs[seq2][marker2]):
            last = seqs[seq1][marker1]
            marker1 += 1
        else:
            last = seqs[seq2][marker2]
            marker2 += 1
    return last


for i in range(n - 1):
    for j in range(i + 1, n):
        print(median(i, j))
        