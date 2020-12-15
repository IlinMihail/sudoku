# sudoku

c = True
num = -1

grid = [
    [9, 0, 2, 6, 1, 7, 0, 0, 4],
    [0, 1, 0, 0, 0, 0, 0, 6, 0],  # 2,3,4,5,9
    [0, 5, 0, 0, 0, 8, 9, 0, 0],
    [0, 0, 0, 1, 0, 0, 2, 0, 0],
    [5, 0, 0, 0, 9, 0, 1, 4, 0],
    [0, 9, 8, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [2, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 3, 0, 0, 5]
]


# Ввод: матрица для вывода, вывод: вывод матрицы
def show_grid(g):
    for r in range(9):
        row = g[r]
        print(row)


# Ввод: матрица с заданием, вывод: решённая матрица
def autosolve(g):
    solved_grid = g.copy()
    p_nums = []
    while not is_solved(solved_grid):
        for y in range(9):
            for x in range(9):
                p_nums = get_nums(solved_grid, x, y)
                if len(p_nums) == 1:
                    print(p_nums)
                    solved_grid[y][x] = p_nums[0]

        show_grid(solved_grid)
        return solved_grid


# Ввод: -, вывод: матрица с заданием
# TODO
def autogenerate():
    print('wip')


# Ввод: матрица, число и координаты ячейки, вывод: Ложь или Истина взависимости от того можно ли поставить это число на выбранных координатах
def check_cell(g, n, x, y):
    x -= 1
    y -= 1
    if n > 9 or n < 1:
        return False

    if g[y][x] != 0:  # Проверка наличия числа на выбранной клетке
        return False

    indx = -1
    indy = -1
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


def get_nums(g, x, y):
    p = []
    for n in range(10):
        if check_cell(g, n, x, y):
            p.insert(0, n)
    return p


def is_solved(g):
    for y in range(9):
        for x in range(9):
            if g[y][x] == 0:
                return False

    return True


print('Судоку v.1.4')
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
        elif val == 'debug':
            # Тесты
            print('Тесты. Должна быть только Правда')
            show_grid(grid)
            print(is_solved(grid) == False)
            print(get_nums(grid, 4, 2) == [9, 5, 4, 3, 2])
            print(check_cell(grid, 1, 8, 8) == True)
            print(check_cell(grid, 1, 2, 2) == False)

        else:
            vals = val.split(',')
            num = int(vals[0])
            x = int(vals[1])
            y = int(vals[2])
            if x < 10 or y < 10:
                if f == True:
                    grid[y][x] = num
                    c = False
                    f = False
                else:
                    if check_cell(grid, num, x, y):
                        grid[y][x] = num
                        c = False
                    else:
                        print('Вы не можете поставить', num, 'здесь')

    show_grid(grid)
    c = True

