# sudoku

c = True
num = -1

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# Ввод: матрица для вывода, вывод: вывод матрицы на экран
def show_grid(g):
    for r in range(9):
        row = g[r]
        print(row)

# Ввод: матрица с заданием, вывод: решённая матрица
def autosolve(g):
    solved_grid = g.copy()
    p_nums = []
    while not is_solved(solved_grid):
        for x in range(9):
            for y in range(9):
                p_nums = get_nums(solved_grid, x, y)
                print(p_nums)
                if len(p_nums) == 1:
                    print('Уникальное число:{0} в {1},{2}'.format(p_nums[0], x, y))
                    solved_grid[y][x] = p_nums[0]

    show_grid(solved_grid)
    return solved_grid


# Ввод: -, вывод: матрица с заданием
# TODO
def autogenerate():
    print('wip')


# Ввод: матрица, число и координаты ячейки, вывод: Ложь или Истина взависимости от того можно ли поставить это число на выбранных координатах
def check_cell(g, n, x, y):
    if n > 9 or n < 1:
        return False

    if g[y][x] != 0:  # Проверка наличия числа на выбранной клетке
        return False

    for indx in range(9):  # Проверка наличия числа в строке
        if indx != x and g[y][indx] == n:
            return False

    for indy in range(9):  # Проверка наличия числа в столбце
        if indy != y and g[indy][x] == n:
            return False

    bx = x // 3
    by = y // 3
    for i in range(by * 3, by * 3 + 3):  # Проверка наличия числа в блоке
        for j in range(bx * 3, bx * 3 + 3):
            if g[i][j] == n and (i, j) != (y, x):
                return False

    return True  # Возврат истины в случае если все условия соблюдены

# Ввод: матрица и координаты ячейки, вывод: возможные числа для этой ячейки
def get_nums(g, x, y):
    p = []
    for n in range(10):
        if check_cell(g, n, x, y):
            p.insert(0, n)
    return p

# Ввод: матрица, вывод: Истина или Ложь взависимости от того решена ли матрица
def is_solved(g):
    for y in range(9):
        for x in range(9):
            if g[y][x] == 0:
                return False
    return True


print('Судоку v.1.5')
show_grid(grid)
while True:
    f = False
    while c == True:
        val = input('Введите число и координаты клетки: ')
        if val == 'solve':
            print('Решаем...')
            autosolve(grid)
        elif val == 'force':
            f = True
        elif val == 'generate':
            autogenerate()
        elif val == 'import':
            c = input('Введите строку: ')
            n = -1
            for y in range(9):
                for x in range(9):
                    n += 1
                    grid[y][x] = int(c[n])

        elif val == 'debug':
            # Тесты
            grid_2 = [
                [9, 0, 2, 6, 1, 7, 0, 0, 4],
                [0, 1, 0, 0, 0, 0, 0, 6, 0],
                [0, 5, 0, 0, 0, 8, 9, 0, 0],
                [0, 0, 0, 1, 0, 0, 2, 0, 0],
                [5, 0, 0, 0, 9, 0, 1, 4, 0],
                [0, 9, 8, 0, 0, 0, 0, 0, 3],
                [0, 0, 0, 0, 4, 0, 0, 0, 0],
                [2, 0, 0, 0, 5, 0, 0, 0, 0],
                [0, 8, 0, 0, 0, 3, 0, 0, 5]
            ]
            print('Тесты. Должна быть только Истина')
            print('Тесты проводятся на сетке:')
            show_grid(grid_2)
            print(is_solved(grid_2) == False)
            print(get_nums(grid_2, 3, 1) == [9,5,4,3,2])
            print(check_cell(grid_2, 1, 7, 7) == True)
            print(check_cell(grid_2, 1, 1, 1) == False)
        else:
            vals = val.split(',')
            num = int(vals[0])
            x = int(vals[1])
            y = int(vals[2])
            x -= 1
            y -= 1
            if x < 0 or y < 0 or x > 9 or y > 9:
                print('Координаты должны быть не меньше 1 и не больше 9')
            else:
                if f == True:
                    grid[y][x] = num
                    c = False
                    f = False
                else:
                    if check_cell(grid, num, x, y):
                        grid[y][x] = num
                        c = False
                    else:
                        print('Вы не можете поставить {0} здесь'.format(num))

    show_grid(grid)
    c = True
