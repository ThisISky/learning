from ctypes import *
import random
import time

# ********************************************************************
# ПЕРЕМЕННЫЕ
# ********************************************************************
valuta = "$"
money = 0
default_money = 10000
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))
play_game = True
round_game = True
six = [1, 10, 19, 28]
seven = [2, 11, 20, 29]
eight = [3, 12, 21, 30]
nine = [4, 13, 22, 31]
ten = [5, 14, 23, 32]
jack = [6, 15, 24, 33]
lady = [7, 16, 25, 34]
king = [8, 17, 26, 35]
ace = [9, 18, 27, 36]
points_player, points_bot = 0, 0
answer_player, answer_bot = "y", "y"
# ********************************************************************
# МЕТОДЫ и ФУНКЦИИ
# ********************************************************************
def win(result):
    color(10)
    print("\n    КОНЕЦ РАУНДА!")
    print(f"    У вас {points_player} очков, а у Альфреда {points_bot}.\n")
    color(14)
    print(f"    Победа за тобой! *Ведьмаку заплатите чеканной монетой*: {result} {valuta}")
    print(f"    У тебя на счету {money}{valuta}")

def loss(result):
    color(10)
    print("\n    КОНЕЦ РАУНДА!")
    print(f"    У вас {points_player} очков, а у Альфреда {points_bot}.\n")
    color(12)
    print(f"    К сожалению, проигрыш: {result} {valuta}")
    print(f"    У тебя на счету {money}{valuta}")

def draw():
    color(11)
    print("\n    КОНЕЦ РАУНДА!")
    print(f"    У вас {points_player} очков, а у Альфреда {points_bot}.\n")
    color(6)
    print(f"    Ничья!")
    print(f"    У тебя на счету {money}{valuta}")

def load_money():
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файл не существует. Задано значение {default_money} {valuta}.")
        m = default_money
    return m

def save_money(money_to_save):
    try:
        f = open("money.dat", "w")
        f.write(str(money_to_save))
        f.close()
    except:
        print("Ошибка создания файла. Наше компания разорилась!")
        quit(0)

def color(c):
    windll.Kernel32.SetConsoleTextAttribute(h, c)

def color_line(c, s):
    for i in range(30):
        print()
    color(c)
    print("*" * (len(s) + 2))
    print("" + s)
    print("*" * (len(s) + 2))

def get_int_input(minimum, maximum, message):
    color(7)
    ret = -1
    while ret < minimum or ret > maximum:
        st = input(message)
        if st.isdigit():
            ret = int(st)
        else:
            print("    Введите целое число!")
    return ret

def get_input(digit, message):
    color(7)
    ret = ""
    while ret == "" or not ret in digit:
        ret = input(message)
    return ret

def card():
    i = random.randint(1, 37)
    if i in six:
        c = "6"
        p = 6
    elif i in seven:
        c = "7"
        p = 7
    elif i in eight:
        c = "8"
        p = 8
    elif i in nine:
        c = "9"
        p = 9
    elif i in ten:
        c = "10"
        p = 10
    elif i in jack:
        c = "Валет"
        p = 2
    elif i in lady:
        c = "Дама"
        p = 3
    elif i in king:
        c = "Король"
        p = 4
    elif i in ace:
        c = "Туз"
        p = 11
    return c, p

def distribution_card(ans_player, answer_bot):
    global card_player, p_player, points_player, card_bot, p_bot, points_bot
    if ans_player == "y" and answer_bot == "y":
        card_player, p_player = card()
        points_player += p_player
        card_bot, p_bot = card()
        points_bot += p_bot
    elif ans_player == "y" and answer_bot == "n":
        card_player, p_player = card()
        points_player += p_player
    elif ans_player == "n" and answer_bot == "y":
        card_bot, p_bot = card()
        points_bot += p_bot

def game_bot():
    global answer_bot
    if points_bot < 17:
        answer_bot = "y"
    elif points_bot >= 17:
        answer_bot = "n"

# ********************************************************************
# ОСНОВНАЯ ЧАСТЬ ПРОГРАММЫ
# ********************************************************************
money = load_money()
start_money = money

while play_game and money > 0:
    color_line(10, "ДОБРО ПОЖАЛОВАТЬ В ИГРУ <<21>>")

    color(6)
    print(" Выберите один из пунктов:")
    print("    1. Начать игру")
    print("    2. Правила игры")
    print("    0. Выход из игры\n")
    color(7)
    x = get_input("012", "    Выбор за тобой: ")
    if x == "0":
        play_game = False
    elif x == "2":
        color_line(10, "ПРАВИЛА ИГРЫ")
        color(14)
        print(" 1. Вам необходимо набрать 21 очко. Перебор означает автоматический проигрыш \n\
    в раунде.")
        print(" 2. В начале игры вам выдается 1 карта, после чего вы можете делать ставку.")
        print(" 3. Вы будете играть против банкующего. Первую ставку делает банкующий. \n\
    Эта ставка будет максимальной для вас.")
        print(" 4. В свой ход вы можете попросить дополнительную карту, если считаете \n\
    нужным, или отказаться от нее.")
        print(" 5. Победа присуждается, если:")
        print("    a) Было набрано 21 очко;")
        print("    b) Очков больше, чем у соперника;")
        print('    c) "Золотое очко" - 2 туза на руках.\n')
        color(7)
        input("    Нажмите Enter, чтобы вернуться на главное меню...")
    elif x == "1":
        round_game = True
        color_line(10, "НАЧИНАЕМ ИГРУ <<21>>")
        color(14)
        print(f" У тебя на счету {money}{valuta}.")
        color(6)
        print(" Против тебя играет банкующий, которого зовут Альфред. \n\
 Можете звать его Альф. Он не против.\n")
        color(2)
        print(" Не будем медлить! Начнем игру!")
        color(7)
        input("    Нажмите Enter, чтобы продолжить...\n")
        while round_game:
            color(14)
            print("    *Альфред перемешивает колоду карт*")
            color(11)
            distribution_card(answer_player, answer_bot)
            for i in range(3):
                print("ZzZ")
                time.sleep(0.7)
                print("zZz")
                time.sleep(0.7)
            while (points_player < 21 and points_bot < 21) and (answer_player == "y" or answer_bot == "y"):
                color(14)
                print("    *Альфред раздает карты*")
                time.sleep(0.7)
                color(2)
                if answer_player == "y":
                    print(f' Выпала карта: "{card_player}". Кол-во очков: {points_player}.')
                    color(7)
                    answer_player = get_input("yn",    "Хотите продолжить брать карты?(y - да, n - нет): ")
                game_bot()
                distribution_card(answer_player, answer_bot)
                if points_player > 21 or points_bot > 21:
                    answer_player, answer_bot = "n", "n"
                    color(12)
                    print("    ПЕРЕБОР!!!")
                    continue
            if points_bot == points_player or points_player > 21 and points_bot > 21:
                draw()
            elif points_player > 21:
                loss(100)
            elif points_bot > 21:
                win(100)
            elif points_bot > points_player:
                loss(100)
            elif points_bot < points_player:
                win(100)
            color(7)
            x = get_input("yn", "    Хотите попробовать ещё?(y - да, n - нет): ")
            if x == "n":
                round_game = False
            else:
                for i in range(30):
                    print()
            points_player, points_bot = 0, 0
            answer_player, answer_bot = "y", "y"


color_line(12, "Жаль, что ты покидаешь нас! Возвращайся скорей!")
color(13)
if money <= 0:
    print(" Упс... Ты остался без денег. Бери кредит и возвращайся ;)")

color(11)
if money > start_money:
    print("Ну что ж, поздравляю с прибылью!")
    print(f"На начало игры у тебя было {start_money}{valuta}.")
    print(f"Сейчас уже {money}{valuta}! Играй ещё и приумножай!")
elif money == start_money:
    print("Ты остался в нуле!")
    print(f"Сумма осталась такой же: {money}{valuta}")
    print("В следующий раз все обязательно получится!")
else:
    print(f"К сожалению, ты проиграл {start_money - money}{valuta}.")
    print("В следующий раз все обязательно получится!")

save_money(money)

color(7)
input("Нажми Enter, чтобы выйти...")
quit()
