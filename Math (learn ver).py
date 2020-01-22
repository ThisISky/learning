import random

lowDiapazon = 10        # Нижняя граница чисел
highDiapazon = 100      # Верхняя граница чисел
sign = 0                # Знак операции
playGame = True         # Главный цикл
count = 0               # Кол-во решенных задач
right = 0               # Правильные ответы
score = 0               # Очки

#========================================================================

print("""Компьютер составил пример. Введите ответ.
Для завершения работы введиет STOP""")

while (playGame):
    print(f"Ваши очки: {score}")
    print(f"Обработано задач: {count}")
    print(f"Правильных ответов: {right}")
    print("-" * 20)

    sign = random.randint(0,3)

    #=================================== СЛОЖЕНИЕ
    if (sign == 0):
        z = random.randint(lowDiapazon, highDiapazon)
        x = random.randint(lowDiapazon, z)
        y = z - x
        if (random.randint(0,1) == 0):
            print(f"{x} + {y} = ...")
        else:
            print(f"{y} + {x} = ...")

    #=================================== ВЫЧИТАНИЕ
    elif (sign == 1):
        x = random.randint(lowDiapazon,highDiapazon)
        y = random.randint(0, x - lowDiapazon)
        z = x - y
        print(f"{x} - {y} = ...")

    #=================================== УМНОЖЕНИЕ
    elif (sign == 2):
        x = random.randint(1, (highDiapazon - lowDiapazon) // random.randint(1, highDiapazon // 10) + 1)
        y = random.randint(lowDiapazon, highDiapazon) // x
        z = x * y
        print(f"{x} * {y} = ...")

    # =================================== ДЕЛЕНИЕ
    elif (sign == 3):
        x = random.randint(1, (highDiapazon - lowDiapazon) // random.randint(1, highDiapazon // 10) + 1)
        y = random.randint(lowDiapazon, highDiapazon) // x
        if (y == 0):
            y = 1
        x = x * y
        z = x // y
        print(f"{x} / {y} = ...")

    user = ""
    while (not user.isdigit()
            and user.upper() != "STOP"
            and user.upper() != "S"
            and user.upper() != "Ы"
            and user.upper() != "ЫЕЩЗ"):
        user = input("Ваш ответ? ")

        if (user.upper() == "HELP"
            and user.upper() != "?"
            and user.upper() != ","
            and user.upper() != "РУДЗ"):
            if (z > 9):
                print(f"Последняя цифра ответа: {z % 10}")
            else:
                print("Ответ состоит из одной цифры, подсказка невозможна")
            score -= 10

        elif (user.upper() == "STOP"
            and user.upper() != "S"
            and user.upper() != "Ы"
            and user.upper() != "ЫЕЩЗ"):
            playGame = False
        else:
            count += 1
            if (int(user) == z):
                print("\nПравильно!\n")
                right += 1
                score += 10
            else:
                print(f"\nОтвет неправильный... Правильно: {z}")
                print(f"Вы можете ввести команду HELP или ?, чтобы увидеть последнюю цифру ответа (-10 очков)\n")
                score -= 20

print("*" * 45);
print("СТАТИСТИКА ИГРЫ:")
print(f"Всего примеров: {count}")
print(f"Правилны ответов: {right}")
print(f"Неправильных ответов: {count - right}")

if (count > 0):
    print(f"Процент верных ответов: {int(right / count * 100)}%")
else:
    print("Процент верных ответов: 0%")
print("Возвращайтесь!")

input()
