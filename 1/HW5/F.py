num_of_classrooms = int(input())
required_power = list(map(int, input().split()))
num_of_conds = int(input())
conds = []
min_price = 1000
total_sum = 0

for _ in range(num_of_conds):
    conds.append(list(map(int, input().split())))
conds.sort(reverse=True)
required_power.sort(reverse=True)

i = 0
j = 0
while j != num_of_classrooms:
    while i != num_of_conds and conds[i][0] >= required_power[j]:
        min_price = min(conds[i][1], min_price)
        i += 1
    total_sum += min_price
    j += 1
print(total_sum)
