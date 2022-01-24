def welcom():
    print("---------------")
    print('Рады приветствовать Вас в игре')
    print('       "Крестики-нолики".')
    print("Формат ввода:")
    print("первая цифра - номер строки, вторая цифра - номер столбца.")
    print("Диапазон каждой координаты от 0 до 2.")
    print('Окончание ввода - клавиша "Enter".')
    print("--------------")

def quad():
    print()
    print("    | 0 | 1 | 2 |")
    print("  ---------------")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")

def ques():
    while True:
        cords = input("          Ваш ход: ").split()

        if len(cords) != 2:
            print("Введите обе координаты!")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Необходимо ввести числа от 0 до 2!")
            continue

        x, y = int(x), int(y)

        if 0 > x or 0 > y or x > 2 or y > 2 :
            print("Координаты вне диапазона! ")
            continue

        if field[x][y] != " "  :
            print(" Клетка занята! ")
            continue
        return x, y

def check():
    for i in range(3):
        sym = []
        for j in range(3):
            sym.append(field[i][j])
        if sym == ["X", "X", "X"]:
            print("Выиграл X. Поздравляем !!!")
            return True
        if sym == ["0", "0", "0"]:
            print("Выиграл 0. Поздравляем !!!")
            return True


    for i in range(3):
        sym = []
        for j in range(3):
            sym.append(field[j][i])
        if sym == ["X", "X", "X"]:
            print("Выиграл X. Поздравляем !!!")
            return True
        if sym == ["0", "0", "0"]:
            print("Выиграл 0. Поздравляем !!!")
            return True

    sym = []
    for i in range(3):
        sym.append(field[i][i])
    if sym == ["X", "X", "X"]:
        print("Выиграл X. Поздравляем !!!")
        return True
    if sym == ["0", "0", "0"]:
        print("Выиграл 0. Поздравляем !!!")
        return True

    sym = []
    for i in range(3):
        sym.append(field[i][2-i])
    if sym == ["X", "X", "X"]:
        print("Выиграл X. Поздравляем !!!")
        return True
    if sym == ["0", "0", "0"]:
        print("Выиграл 0. Поздравляем !!!")
        return True
    return False

welcom()
field = [[" "] * 3 for i in range (3)]
count = 0
while True:
    count += 1

    quad()

    if count % 2 == 1:
        print("Ходит X. Введите через пробел номер строки и номер столбца.")
        print('Диапазон каждой координаты от 0 до 2. Окончание ввода - клавиша "Enter".')
    else:
        print("Ходит 0. Введите через пробел номер строки и номер столбца.")
        print('Диапазон каждой координаты от 0 до 2. Окончание ввода - клавиша "Enter".')

    x, y = ques()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check():
        break

    if count == 9:
        print("Ничья")
        break



