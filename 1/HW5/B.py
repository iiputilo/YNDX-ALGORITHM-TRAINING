num_of_cars, k = map(int, input().split())
car_nums = list(map(int, input().split()))
pref_sum = [0] * (num_of_cars + 1)
for i in range(num_of_cars):
    pref_sum[i+1] = pref_sum[i] + car_nums[i]


def counter(pref_sum, num_of_cars, k):
    right = 0
    k_counter = 0
    for left in range(num_of_cars + 1):
        while right < num_of_cars + 1 and pref_sum[right] - pref_sum[left] < k:
            right += 1
        if right == num_of_cars + 1:
            break
        if pref_sum[right] - pref_sum[left] == k:
            k_counter += 1
    return k_counter


print(counter(pref_sum, num_of_cars, k))
