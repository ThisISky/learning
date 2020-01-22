from ctypes import *
import random
import time

valuta = "$"
money = 0
default_money = 10000
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
playGame = True

# ================================================================================

# Вывод сообщения о выигрыше
def win(result):
    color(14)
    print(f"    Победа за тобой! *Ведьмаку заплатите чеканной монетой*: {result} {valuta}")
    print(f"    У тебя на счету {money} {valuta}")

# Вывод сообщения о проигрыше
def loss(result):
    color(12)
    print(f"    К сожалению, проигрыш: {result} {valuta}")
    print(f"    У тебя на счету {money} {valuta}")

# Чтение из файла оставшейся суммы
def load_money():
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файл не существует. Задано значение {default_money} {valuta}.")
        m = default_money
    return m

# Запись суммы в файл
def save_money(moneyToSave):
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except:
        print("Ошибка создания файла. Наше Казино закрывается!")
        quit(0)

# Установка цвета текста
def color(c):
    windll.Kernel32.SetConsoleTextAttribute(h, c)

# Вывод на экран цветного, обрамленного звездочками текст
def colorLine(c, s):
    for i in range(30):
        print()
    color(c)
    print("*" * (len(s) + 2))
    print("" + s)
    print("*" * (len(s) + 2))

# Функция ввода целого числа
def getIntInput(minimum, maximum, message):
    color(7)
    ret = -1
    while ret < minimum or ret > maximum:
        st = input(message)
        if st.isdigit():
            ret = int(st)
        else:
            print("    Введите целое число!")
    return ret

# Функция ввода значения
def getInput(digit, message):
    color(7)
    ret = ""
    while ret == "" or not ret in digit:
        ret = input(message)
    return ret

# ================================================================================

# Главный цикл
def main():
    global money, playGame

    money = load_money()
    start_money = money

    while playGame and money > 0:
        colorLine(10, "Приветствую тебя в нашем заведении 'Азино 777' !")
        color(14)
        print(f" У тебя на счету {money} {valuta}.")

        color(6)
        print(" Ты можешь сыграть в:")
        print("    1. Рулетка")
        print("    2. Кости")
        print("    3. Однорукий бандит")
        print("    0. Выход. Ставка 0 в играх - выход\n")
        color(7)

        x = getInput("01234", "    Твой выбор? ")
        if x == "0":
            playGame = False
        elif x == "1":
            roulette()
        elif x == "2":
            dice()
        elif x == "3":
            one_hand_bandit()


    colorLine(12, "Жаль, что ты покидаешь нас! Возвращайся скорей!")
    color(13)
    if money <= 0:
        print(" Упс... Ты остался безе денег. Возьми микрокредит и возвращайся!")

    color(11)
    if money > start_money:
        print("Ну что ж, поздравляю с прибылью!")
        print(f"На начало игры у тебя было {start_money} {valuta}.")
        print(f"Сейчас уже {money} {valuta}! Играй ещё и приумножай!")
    elif money == start_money:
        print("Ты остался в нуле!")
        print(f"Сумма осталась такой же: {money} {valuta}")
        print("В следующий раз все обязательно получится!")
    else:
        print(f"К сожалению, ты проиграл {start_money - money} {valuta}.")
        print("В следующий раз все обязательно получится!")

    save_money(money)

    color(7)            # Устанавливаем цвет консоли на стандартный
    input("Нажми Enter, чтобы выйти...")
    quit()              # Выход

# Анимация рулетки
def getRoulette(visable):
    tickTime = random.randint(100, 200) / 10000
    mainTime = 0
    number = random.randint(0, 38)
    increaseTickTime = random.randint(100, 110) / 100
    col = 1

    while mainTime < 0.7:
        col += 1
        if col > 15:
            col = 1

        mainTime += tickTime
        tickTime *= increaseTickTime

        color(col)
        number += 1
        if number > 38:
            number = 0
            print()
        printNumber = number
        if number == 37:
            printNumber = "00"
        elif number == 38:
            printNumber = "000"

        print(" Число >",
              printNumber,
              "*" * number,
              " " * (79 - number * 2),
              "*" * number)

        if visable:
            time.sleep(mainTime)
    return number

# Анимация костей
def getDice():
    count = random.randint(3, 8)
    sleep = 0
    while count > 0:
        color(count + 7)
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(" " * 10, "----- -----")
        print(" " * 10, f"| {x} | | {y} |")
        print(" " * 10, "----- -----")
        time.sleep(sleep)
        sleep += 1 / count
        count -= 1
    return x + y

# Подсчет однорукого бандита
def getMaxCount(digit, v1, v2, v3, v4, v5):
    ret = 0
    if digit == v1:
        ret += 1
    if digit == v2:
        ret += 1
    if digit == v3:
        ret += 1
    if digit == v4:
        ret += 1
    if digit == v5:
        ret += 1
    return ret

# Анимация однорукого бандита
def getOHBRes(stavka):
    res = stavka
    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0

    get_d1 = True
    get_d2 = True
    get_d3 = True
    get_d4 = True
    get_d5 = True
    col = 10

    while get_d1 or get_d2 or get_d3 or get_d4 or get_d5:
        if get_d1:
            d1 += 1
        if get_d2:
            d2 -= 1
        if get_d3:
            d3 += 1
        if get_d4:
            d4 -= 1
        if get_d5:
            d5 += 1

        if d1 > 9:
            d1 = 0
        if d2 < 0:
            d2 = 9
        if d3 > 9:
            d3 = 0
        if d4 < 0:
            d4 = 9
        if d5 > 9:
            d5 = 0

        if random.randint(0, 20) == 1:
            get_d1 = False
        if random.randint(0, 20) == 1:
            get_d2 = False
        if random.randint(0, 20) == 1:
            get_d3 = False
        if random.randint(0, 20) == 1:
            get_d4 = False
        if random.randint(0, 20) == 1:
            get_d5 = False

        time.sleep(0.1)
        color(col)
        col += 1
        if col > 15:
            col = 10

        print("    " + "%" * 10)
        print(f"    {d1} {d2} {d3} {d4} {d5}")

    max_count = getMaxCount(d1, d1, d2, d3, d4, d5)
    if max_count < getMaxCount(d2, d1, d2, d3, d4, d5):
        max_count = getMaxCount(d2, d1, d2, d3, d4, d5)
    if max_count < getMaxCount(d3, d1, d2, d3, d4, d5):
        max_count = getMaxCount(d3, d1, d2, d3, d4, d5)
    if max_count < getMaxCount(d4, d1, d2, d3, d4, d5):
        max_count = getMaxCount(d4, d1, d2, d3, d4, d5)
    if max_count < getMaxCount(d5, d1, d2, d3, d4, d5):
        max_count = getMaxCount(d5, d1, d2, d3, d4, d5)

    color(14)
    if max_count == 2:
        print(f" Совпадение двух чисел! Твой выигрыш в размере ставки: {res} {valuta}.")
    elif max_count == 3:
        res *= 2
        print(f" Совпадение трех чисел! Твой выигрыш 2:1: {res} {valuta}.")
    elif max_count == 4:
        res *= 5
        print(f" Совпадение четырех чисел! Твой выигрыш 5:1: {res} {valuta}.")
    elif max_count == 5:
        res *= 10
        print(f" БИНГО! Совпадение всех чисел! Твой выигрыш 10:1: {res} {valuta}.")
    else:
        loss(res)
        res = 0

    color(11)
    print()
    input(" Нажмите Enter для продолжения...")

    return res

# ================================================================================

# Рулетка
def roulette():
    global money
    playGame = True
    while playGame and money > 0:
        colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ")
        color(14)
        print(f"\n У тебя на счету {money} {valuta}.\n")
        color(11)
        print(" Ставлю на ...")
        print("    1. Четное (выигрыш 1:1)")
        print("    2. Нечетное (выигрыш 1:1)")
        print("    3. Дюжина (выигрыш 3:1)")
        print("    4. Число (выигрыш 36:1")
        print("    0. Возврат в меню\n")

        x = getInput("01234", "    Твой выбор? ")
        play_roulette = True

        if x == "3":
            color(2)
            print()
            print(" Выбери диапозон:...")
            print("    1. От 0 до 12")
            print("    2. От 13 до 24")
            print("    3. От 25 до 36")
            print("    0. Назад\n")

            duzhina = getInput("0123", "    Твой выбор? ")

            if duzhina == "1":
                text_duzhina = "от 0 до 12"
            elif duzhina == "2":
                text_duzhina = "от 13 до 24"
            elif duzhina == "3":
                text_duzhina = "от 25 до 36"
            elif duzhina == "0":
                play_roulette = False

        elif x == "4":
            chislo = getIntInput(0, 36, "    На какое число ставишь (0..36)? ")

        color(7)
        if x == "0":
            return 0

        if play_roulette:
            stavka = getIntInput(0, money, f"    Сколько поставишь (не больше {money} {valuta})? ")
            if stavka == 0:
                return 0

            number = getRoulette(True)

            if x == "1":
                print("    Ты поставил на ЧЕТНОЕ!")
                if number < 37 and number % 2 == 0:
                    money += stavka
                    win(stavka)
                else:
                    money -= stavka
                    loss(stavka)
            elif x == "2":
                print("    Ты поставил на НЕЧЕТНОЕ!")
                if number < 37 and number % 2 != 0:
                    money += stavka
                    win(stavka)
                else:
                    money -= stavka
                    loss(stavka)
            elif x == "3":
                print(f"    Ставка сделана на диапазон чисел {text_duzhina}.")
                winDuzhina = ""
                if number < 13:
                    winDuzhina = "1"
                elif 12 < number < 25:
                    winDuzhina = "2"
                elif number > 24:
                    winDuzhina = "3"

                if duzhina == winDuzhina:
                    money += stavka * 2
                    win(stavka * 3)
                else:
                    money -= stavka
                    loss(stavka)
            elif x == "4":
                print(f"    Ставка сделана на число {chislo}.")
                if number == chislo:
                    money += stavka * 35
                    win(stavka * 36)
                else:
                    money -= stavka
                    loss(stavka)

            print()
            input(" Нажмите Enter для продолжения...")

# Кости
def dice():
    global money
    playGame = True

    while playGame:
        print()
        colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В КОСТИ!")
        color(14)
        print(f"\n У тебя на счету {money} {valuta}.")

        color(7)
        stavka = getIntInput(0, money, f"    Сделай ставку в пределах {money} {valuta}: ")
        if stavka == 0:
            return 0

        playRound = True
        control = stavka
        oldResult = getDice()
        firstPlay = True

        while playRound and stavka > 0 and money > 0:
            if stavka > money:
                stavka = money
            color(11)
            print(f"\n    В твоем распоряжении {stavka} {valuta}.")
            color(12)
            print(f"\n    Текущая сумма чисел на костях: {oldResult}.")
            color(11)
            print("\n    Сумма чисел на гранях будет больше, меньше или равна предыдущей?")
            color(7)
            x = getInput("0123", "    Введите 1 - больше, 2 - меньше, 3 - равна или 0 - выход: ")

            if x != "0":
                firstPlay = False
                if stavka > money:
                    stavka = money

                money -= stavka
                diceResult = getDice()

                win = False
                if (oldResult > diceResult and x == "2") or (oldResult < diceResult and x == "1"):
                    win = True

                if not x == "3":
                    if win:
                        money += stavka + stavka // 5
                        color(14)
                        print(f"    Победа за тобой! *Ведьмаку заплатите чеканной монетой*: {stavka // 5} {valuta}")
                        stavka += stavka // 5
                    else:
                        stavka = control
                        loss(stavka)
                elif x == "3":
                    if oldResult == diceResult:
                        money += stavka * 3
                        win(stavka * 3)
                        stavka *= 3
                    else:
                        stavka = control
                        loss(stavka)

                oldResult = diceResult

            else:
                if firstPlay:
                    money -= stavka
                playRound = False

# Однорукий бандит
def one_hand_bandit():
    global money
    playGame = True

    while playGame:
        colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В ОДНОРУКОГО БАНДИТА!")
        color(14)
        print(f"\n У тебя на счету {money} {valuta}.\n")
        color(5)
        print(" Правила игры:")
        print("    1. При совпадении 2-х чисел ставка не списывается.")
        print("    2. При совпадении 3-х чисел выигрыш 2:1.")
        print("    3. При совпадении 4-х чисел выигрыш 5:1.")
        print("    4. При совпадении 5-ти чисел выигрыш 10:1.")
        print("    5. Ставка 0 для завершении игры.\n")

        stavka = getIntInput(0, money, f"    Введите ставку от 0 до {money} {valuta}: ")

        if stavka == 0:
            return 0

        money -= stavka
        money += getOHBRes(stavka)

        if (money <= 0):
            playGame = False


# ================================================================================
# ================================================================================

main()