k = int(input())
seq = [x for x in input()]
beneficial_ways = 0
strike = 0
for i in range(k, len(seq)):
    if seq[i] == seq[i-k]:
        strike += 1
        beneficial_ways += strike
    else:
        strike = 0
print(beneficial_ways)
