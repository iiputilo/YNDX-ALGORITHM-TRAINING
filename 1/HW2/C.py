len_arr, arr, x = int(input()), tuple(map(int, input().split())), int(input())


def nearest_element(length, array, target):
    nearest_element_diff, nearest_element_val = abs(target - array[0]), array[0]
    for num in range(1, length):
        diff = abs(target - array[num])
        if diff < nearest_element_diff:
            nearest_element_diff = diff
            nearest_element_val = array[num]
    return nearest_element_val


print(nearest_element(len_arr, arr, x))
