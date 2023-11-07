num_of_strings = int(input())
set_x = set()
for i in range(num_of_strings):
    x, y = map(int, input().split())
    set_x.add(x)
print(len(set_x))
