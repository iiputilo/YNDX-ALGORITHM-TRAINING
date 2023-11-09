bank_accounts = dict()
account_holders = []


def bank_account_operation(operation, name1=None, name2=None, amount=0):
    if operation == 'BALANCE':
        if name1 in bank_accounts:
            print(bank_accounts[name1])
        else:
            print('ERROR')
    if operation == 'INCOME':
        for holder in account_holders:
            if bank_accounts[holder] > 0:
                bank_accounts[holder] += int((amount * 0.01 * bank_accounts[holder]))
    if operation == 'WITHDRAW':
        if name1 not in bank_accounts:
            bank_accounts[name1] = 0
            account_holders.append(name1)
        bank_accounts[name1] -= amount
    if operation == 'DEPOSIT':
        if name1 not in bank_accounts:
            bank_accounts[name1] = amount
            account_holders.append(name1)
        else:
            bank_accounts[name1] += amount
    if operation == 'TRANSFER':
        if name1 not in bank_accounts:
            bank_accounts[name1] = 0
            account_holders.append(name1)
        if name2 not in bank_accounts:
            bank_accounts[name2] = 0
            account_holders.append(name2)
        bank_accounts[name1] -= amount
        bank_accounts[name2] += amount


with open('input.txt') as file:
    for line in file:
        current_operation = line.split()
        if current_operation[0] == 'INCOME':
            bank_account_operation(current_operation[0], amount=int(current_operation[1]))
        elif current_operation[0] == 'BALANCE':
            bank_account_operation(current_operation[0], name1=current_operation[1])
        elif current_operation[0] == 'TRANSFER':
            bank_account_operation(current_operation[0], name1=current_operation[1],
                                   name2=current_operation[2], amount=int(current_operation[3]))
        else:
            bank_account_operation(current_operation[0], name1=current_operation[1], amount=int(current_operation[2]))
