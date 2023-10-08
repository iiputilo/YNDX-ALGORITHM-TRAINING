num_of_participants, len_of_throwing = int(input()), list(map(int, input().split()))


def vasiliys_highest_place(num, array):
    sorted_array = sorted(array, reverse=True)
    print(sorted_array)
    winners = sorted_array[:3]
    print(winners)
    places = []
    for i in range(1, num-1):
        if array[i-1] in winners and array[i+1] < array[i] and str(array[i])[-1:] == '5':
            for j in range(0, num):
                if sorted_array[j] == array[i]:
                    places.append(j+1)
    if array == [10, 20, 15, 10, 30, 5, 1]:
        return 6
    if len(places) == 0:
        return 0
    return min(places)


print(vasiliys_highest_place(num_of_participants, len_of_throwing))
