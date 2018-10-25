from tkinter import *

import brain

root = Tk()
root.title("Морской бой (помощник)")
x_screen = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y_screen = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry("+%d+%d" % (x_screen, y_screen))


def new_game(event):
    for x in range(10):
        horizontal_line[i]["bg"] = "SystemButtonFace"
        vertical_line[i]["bg"] = "SystemButtonFace"
        for y in range(10):
            pole[x][y].set(0)
            cell[x][y]["bg"] = "SystemButtonFace"


def calculate(event):  # подсчет кораблей
    for index_i in range(10):  # обновление границы
        horizontal_line[index_i]["bg"] = "SystemButtonFace"
        vertical_line[index_i]["bg"] = "SystemButtonFace"
    max_maybe = max_open = max_index_x = max_index_y = -1
    for pos_x in range(10):
        for k in range(10):
            if pole[pos_x][k].get() == 1:
                cell[pos_x][k]["bg"] = "#808080"
            else:
                cell[pos_x][k]["bg"] = "SystemButtonFace"

            try:
                length_ship = int(entry_size.get())
            except ValueError:
                length_ship = 4
                entry_size.insert(0, "4")

            if not pole[pos_x][k].get():
                brain.sum_open_cells[pos_x][k] = brain.count_empty(pole, pos_x, k)
            else:
                brain.sum_open_cells[pos_x][k] = 0
            brain.sum_possible_ship[pos_x][k] = brain.count_ship(pole, pos_x, k, length_ship)
            brain.sum_possible_ship[pos_x][k] += brain.count_ship(pole, pos_x, k, length_ship - 1)
            brain.sum_possible_ship[pos_x][k] += brain.count_ship(pole, pos_x, k, length_ship - 2)
            # отображение на ячейках
            if checkbutton_empty_value.get():
                cell[pos_x][k]["text"] = brain.sum_open_cells[pos_x][k]
                if brain.sum_possible_ship[pos_x][k] > max_maybe:
                    max_maybe = brain.sum_possible_ship[pos_x][k]
                    max_open = brain.sum_open_cells[pos_x][k]
                    max_index_x, max_index_y = pos_x, k
                elif brain.sum_possible_ship[pos_x][k] == max_maybe and \
                        brain.sum_open_cells[pos_x][k] > max_open:
                    max_maybe = brain.sum_possible_ship[pos_x][k]
                    max_open = brain.sum_open_cells[pos_x][k]
                    max_index_x, max_index_y = pos_x, k
            else:
                cell[pos_x][k]["text"] = str(brain.sum_possible_ship[pos_x][k])
                if brain.sum_possible_ship[pos_x][k] > max_maybe:
                    max_maybe = brain.sum_possible_ship[pos_x][k]
                    max_index_x, max_index_y = pos_x, k
        print(brain.sum_possible_ship[pos_x])  # вывод на экран

    print()
    for index_i in range(10):
        print(brain.sum_open_cells[index_i])

    # алгоритм
    horizontal_line[max_index_y]["bg"] = "yellow"
    vertical_line[max_index_x]["bg"] = "yellow"
    cell[max_index_x][max_index_y]["bg"] = "Red"
    print("Бей по:", max_index_x + 1, max_index_y + 1)


# объекты
horizontal_line, vertical_line = [], []  # границы
hor = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
for i in range(10):
    horizontal_line.append(Label(text=hor[i]))
    vertical_line.append(Label(text=str(i + 1), justify=LEFT))

pole, cell = [], []  # ячейки
for x in range(10):
    cell.append([])
    pole.append([])
    for y in range(10):
        pole[x].append(BooleanVar())
        cell[x].append(Checkbutton(text="", variable=pole[x][y],
                                   onvalue=1, offvalue=0))

# оставшиеся объекты
label_size = Label(text="Размер корабля")  # наклейка размера
entry_size = Entry(width=5, justify=CENTER)  # размер корабля
label_empty = Label(text="Подсчет клеток вокруг")
checkbutton_empty_value = BooleanVar()
checkbutton_empty = Checkbutton(variable=checkbutton_empty_value,
                                onvalue=1, offvalue=0)
button_calc = Button(text="Расчет позиции")  # кнопка для подсчета
button_clear = Button(text="Новая игра")

# бинд основной кнопки
button_calc.bind('<Button-1>', calculate)
button_clear.bind('<Button-1>', new_game)

# размещение объектов


for i in range(10):  # границы
    horizontal_line[i].grid(row=0, column=i + 1)
    vertical_line[i].grid(row=i + 1, column=0)

for i in range(10):  # ячейки
    for j in range(10):
        cell[i][j].grid(row=i + 1, column=j + 1)

label_size.grid(row=0, column=11)
entry_size.grid(row=1, column=11)
button_calc.grid(row=2, column=11)
label_empty.grid(row=4, column=11)
checkbutton_empty.grid(row=5, column=11)

# button_clear.grid(row=9, column=11)

root.mainloop()
