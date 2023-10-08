def more_than_neighbours(seq):
    count = 0
    for num in range(1, len(seq)-1):
        if seq[num-1] < seq[num] > seq[num+1]:
            count += 1
    return count


print(more_than_neighbours(tuple(map(int, input().split()))))
