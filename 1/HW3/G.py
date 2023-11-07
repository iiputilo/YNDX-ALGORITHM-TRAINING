n = int(input())
turtle_say = []
for _ in range(n):
    turtle_say.append(input())


def liar_turtles(m):
    variants = [x for x in range(len(m))]
    variants_rev = variants[::-1]
    correct_answers = dict()
    for x in range(len(m)):
        if f'{variants[x]} {variants_rev[x]}' not in correct_answers:
            correct_answers[f'{variants[x]} {variants_rev[x]}'] = 0
    num_of_lies = 0
    for y in m:
        if y in correct_answers:
            if correct_answers[y] == 0:
                correct_answers[y] += 1
            else:
                num_of_lies += 1
        else:
            num_of_lies += 1
    return len(m) - num_of_lies


print(liar_turtles(turtle_say))
