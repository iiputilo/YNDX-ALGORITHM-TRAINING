field_params = list(map(int, input().split()))
mine_coordinates = []
for _ in range(field_params[2]):
    mine_coordinates.append(list(map(int, input().split())))


def create_minesweeper_field(f_params, mine_coords):
    field = []
    string = []
    for _ in range(f_params[1]):
        string.append(0)
    for _ in range(f_params[0]):
        string_copy = string.copy()
        field.append(string_copy)
    for coord in mine_coords:
        flag1 = False
        flag2 = False
        if coord[0] - 1 != 0:
            field[coord[0] - 2][coord[1] - 1] += 1
            flag1 = True
        if coord[0] + 1 <= f_params[0]:
            field[coord[0]][coord[1] - 1] += 1
            flag2 = True
        if coord[1] - 1 != 0:
            field[coord[0] - 1][coord[1] - 2] += 1
            if flag1:
                field[coord[0] - 2][coord[1] - 2] += 1
            if flag2:
                field[coord[0]][coord[1] - 2] += 1
        if coord[1] + 1 <= f_params[1]:
            field[coord[0] - 1][coord[1]] += 1
            if flag1:
                field[coord[0] - 2][coord[1]] += 1
            if flag2:
                field[coord[0]][coord[1]] += 1
    for coord in mine_coords:
        field[coord[0] - 1][coord[1] - 1] = '*'
    for num_of_str in range(len(field)):
        print(' '.join(map(str, field[num_of_str])))


create_minesweeper_field(field_params, mine_coordinates)

