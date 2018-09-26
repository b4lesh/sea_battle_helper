sum_possible_ship = [[0 for i in range(10)] for j in range(10)]
sum_open_cells = [[0 for i in range(10)] for j in range(10)]


def count_ship(pole, x, y, length_ship):
    count = 0
    for i in range(length_ship):
        empty = True
        tmp = x - i
        for j in range(length_ship):
            if (0 <= tmp + j <= 9) and (not pole[tmp + j][y].get()):
                pass
            else:
                empty = False
                break
        if empty:
            count += 1

    for i in range(length_ship):
        empty = True
        tmp = y - i
        for j in range(length_ship):
            if (0 <= tmp + j <= 9) and (not pole[x][tmp + j].get()):
                pass
            else:
                empty = False
                break
        if empty:
            count += 1
    return count


def count_empty(pole, x, y):
    count = 0
    tmp_x, tmp_y = x - 1, y - 1
    for i in range(3):
        for j in range(3):
            if (0 <= tmp_x + i <= 9) and (0 <= tmp_y + j <= 9) and \
                    (not pole[tmp_x + i][tmp_y + j].get()):
                count += 1

    return count
