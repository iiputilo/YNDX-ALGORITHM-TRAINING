number_of_notes = int(input())
frequencies = []
while len(frequencies) != number_of_notes:
    frequencies.append(list(map(str, input().split())))


def triangle_frequency_finder(freq):
    left = 30.0
    right = 4000.0
    prev = float(frequencies[0][0])
    for i in range(1, len(frequencies)):
        now = float(frequencies[i][0])
        if abs(prev - now) < 10 ** -6:
            continue
        elif frequencies[i][1] == 'closer':
            if now < prev:
                right = min(right, (now + prev) / 2)
            else:
                left = max(left, (now + prev) / 2)
        else:
            if now > prev:
                right = min(right, (now + prev) / 2)
            else:
                left = max(left, (now + prev) / 2)
        prev = now
    return str(f'{left} {right}')


print(triangle_frequency_finder(frequencies))
