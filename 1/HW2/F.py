seq_len, seq = int(input()), list(map(int, input().split()))


def symmetrical(len_of_sequence, sequence):
    if sequence == list(reversed(sequence)):
        return 0
    for i in range(1, len_of_sequence):
        if sequence + list(reversed(sequence))[-i:] == list(reversed(sequence + list(reversed(sequence))[-i:])):
            return f'{i}\n{" ".join(map(str, list(reversed(sequence[:i]))))}'


print(symmetrical(seq_len, seq))
