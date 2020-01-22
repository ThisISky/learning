import random

play_game = True                                                                            # Отвечает за начало и конец игры
money = 5000                                                                                # Кол-во денег у игрока
num = 0                                                                                     # Число, которое выдает компьютер
color = 0                                                                                   # Цвет, который выдает компьютер
color_players = 0                                                                           # Цвет, который выбрал игрок
colorNum_Red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]          # Список номеров с красной ячейкой
colorNum_Black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]       # Список номеров с черной ячейкой

# ===========================================================

print(f"""Добро пожаловать в русскую рулетку!

Правила игры:
В начале игры вам выдается {money} $ для ставок.
В начале хода вам необходимо указать номер игровой зоны.
Если на счету у вас остлось 0 $ - вы проиграли.
Если вы хотите прекратить игру -  введите STOP.

Удачной игры!""")
print("-" * 40)

while(play_game):

    while (True):
        color = random.randint(0, 2)
        if (color == 1):
            color = "Red"
            num = colorNum_Red[random.randint(0, len(colorNum_Red)-1)]
            break
        elif (color == 2):
            color = "Black"
            num = colorNum_Black[random.randint(0, len(colorNum_Black)-1)]
            break
        elif (color == 0):
            color = random.randint(0, 5)
            if (color == 0):
                num = 0
                color = "Green"
                break

    print(color, num)

    print(f"Ваши деньги: {money} $")
    print("-" * 40)

    num_players = ""
    while (not num_players.isdigit()
            and num_players.upper() != "STOP"
            and num_players.upper() != "S"
            and num_players.upper() != "Ы"
            and num_players.upper() != "ЫЕЩЗ"):
        while (True):
            num_players = input("Введие число от 0 до 36: ")
            if (num_players.upper() == "STOP"
                    or num_players.upper() == "S"
                    or num_players.upper() == "Ы"
                    or num_players.upper() == "ЫЕЩЗ"):
                    play_game = False
            elif (int(num_players) < 0 or int(num_players) > 36):
                print("Ваше число не входит в диапозон от 0 до 36.")
            else:
                while (True):
                    rate = int(input("Введите вашу ставку: "))
                    if (rate > money):
                        print("Ваша ставка не может превышать кол-ва ваших денег.")
                    else:
                        break

                print("-" * 40)
                print(f"Выпало {color} {num}.")

                if (num == int(num_players)):
                    money += rate * 36
                    print(f"Поздравляю! Вы выиграли {rate * 36} $.")
                elif (num != int(num_players)):
                    money -= rate
                    print(f"К сожалению, вы проиграли {rate} $.")

                if (money <= 0):
                    print("-" * 40)
                    print("У вас закончились деньги. Вы проиграли.")
                    play_game = False
            break

print("-" * 40)
print(f"""Спасибо за игру!
Ваш выигрыш составил {money} $.

Ждем вас в следующий раз!""")

input()