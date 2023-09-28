temp = list(map(int, input().split()))
mode = input()

if mode == 'freeze':
    if temp[0] < temp[1]:
        print(temp[0])
    else:
        print(temp[1])
if mode == 'heat':
    if temp[0] > temp[1]:
        print(temp[0])
    else:
        print(temp[1])
if mode == 'auto':
    print(temp[1])
if mode == 'fan':
    print(temp[0])
