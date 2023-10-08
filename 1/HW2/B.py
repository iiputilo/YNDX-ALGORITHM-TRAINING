def seq_type(seq):
    repeats = 0
    ascending_check = 0
    descending_check = 0
    num_prev = seq[0]
    for num in range(1, len(seq)):
        if seq[num] < num_prev:
            descending_check += 1
            num_prev = seq[num]
        elif seq[num] > num_prev:
            ascending_check += 1
            num_prev = seq[num]
        elif seq[num] == num_prev:
            repeats += 1
    if repeats == len(seq) - 1:
        return 'CONSTANT'
    elif descending_check == len(seq) - 1:
        return 'DESCENDING'
    elif ascending_check == len(seq) - 1:
        return 'ASCENDING'
    elif ascending_check and descending_check > 0:
        return 'RANDOM'
    elif (ascending_check and repeats > 0) and descending_check == 0:
        return 'WEAKLY ASCENDING'
    else:
        return 'WEAKLY DESCENDING'


sequence = []
sequence_create = True
while sequence_create:
    seq_part = int(input())
    if seq_part != -2 * (10 ** 9):
        sequence.append(seq_part)
    else:
        sequence_create = False

print(seq_type(sequence))
