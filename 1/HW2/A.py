def is_growing(seq):
    num_0 = seq[0]
    for num in range(1, len(seq)):
        if seq[num] > num_0:
            num_0 = seq[num]
        elif seq[num] <= num_0:
            return 'NO'
    return 'YES'


print(is_growing(tuple(map(int, input().split()))))
