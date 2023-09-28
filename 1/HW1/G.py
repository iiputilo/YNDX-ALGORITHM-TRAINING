n, k, m = map(int, input().split())


def divider(num1, num2):
    if num1 // num2 == num1 / num2 and num1 // num2 > 0:
        return [num1 // num2, 0]
    elif num1 // num2 != num1 / num2 and num1 // num2 > 0:
        remainder = num1 - ((num1 // num2) * num2)
        return [num1 // num2, remainder]
    else:
        return [0, 0]


parts = 0
while n // k > 0:
    n, blanks = divider(n, k)[1], divider(n, k)[0]
    n, parts = n + (divider(k, m)[1] * blanks), parts + (divider(k, m)[0] * blanks)
print(parts)
