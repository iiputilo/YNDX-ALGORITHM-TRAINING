with open('input.txt') as file:
    parameters = file.read().splitlines()
    amounts = dict()
    for param in parameters:
        name, product, amount = param.split()
        key = f'{name} {product}'
        if key in amounts:
            amounts[key] += int(amount)
        else:
            amounts[key] = int(amount)
    e = sorted(list(amounts.items()))
    output_name = e[0][0].split()[0]
    print(f'{output_name}:')
    for index in range(len(e)):
        if output_name == e[index][0].split()[0]:
            print(e[index][0].split()[1], e[index][1])
        else:
            output_name = e[index][0].split()[0]
            print(f'{output_name}:')
            print(e[index][0].split()[1], e[index][1])
