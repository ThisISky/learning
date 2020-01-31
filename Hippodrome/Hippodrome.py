from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint


# ********************************************************************
# МЕТОДЫ и ФУНКЦИИ
# ********************************************************************
def setup_horse():
    global state01, state02, state03, state04
    global weather, time_day
    global win_coef01, win_coef02, win_coef03, win_coef04
    global play01, play02, play03, play04
    global reverse01, reverse02, reverse03, reverse04
    global fast_speed01, fast_speed02, fast_speed03, fast_speed04

    # Погода (1 - ливень, .., безоблачно)
    weather = randint(1, 5)
    # Время суток (1 - ночь, .., 4 - вечер)
    time_day = randint(1, 4)

    # Состояние лошади (1 - великолепно, .., 5 - ужасно больна)
    state01 = randint(1, 5)
    state02 = randint(1, 5)
    state03 = randint(1, 5)
    state04 = randint(1, 5)

    win_coef01 = int(100 + randint(1, 30 + state01 * 60)) / 100
    win_coef02 = int(100 + randint(1, 30 + state02 * 60)) / 100
    win_coef03 = int(100 + randint(1, 30 + state03 * 60)) / 100
    win_coef04 = int(100 + randint(1, 30 + state04 * 60)) / 100

    reverse01 = False
    reverse02 = False
    reverse03 = False
    reverse04 = False

    play01 = True
    play02 = True
    play03 = True
    play04 = True

    fast_speed01 = False
    fast_speed02 = False
    fast_speed03 = False
    fast_speed04 = False

def win_round(horse):
    global x01, x02, x03, x04
    global money

    res = 'К финишу пришла лошадь '
    if horse == 1:
        res += f'{nameHorse01}. '
        win = summ01.get() * win_coef01
    elif horse == 2:
        res += f'{nameHorse02}. '
        win = summ02.get() * win_coef02
    elif horse == 3:
        res += f'{nameHorse03}. '
        win = summ03.get() * win_coef03
    elif horse == 4:
        res += f'{nameHorse04}. '
        win = summ04.get() * win_coef04

    if horse > 0:
        res += f'Вы выиграли {int(win)} {valuta}. '
        if win > 0:
            res += 'Поздравляем! Средства уже зачислены на ваш счёт!'
            insertText(f'Этот забег принес Вам {int(win)} {valuta}.')
        else:
            res += 'К сожалению, Ваша лошадь была неправильной. Попробуйте ещё раз!'
            insertText('Делайте ставку! Увеличивайте прибыль!')
        messagebox.showinfo('Результат', res)
    else:
        messagebox.showinfo('Всё плохо', 'До финиша не дошёл никто. Забег призван несостоявшимся. Все ставки возвращены.')
        insertText('Забег признан состоявшимся.')
        win = summ01.get() + summ02.get() + summ03.get() + summ04.get()

    money += win
    saveMoney(int(money))

    setup_horse()

    startButton['state'] = 'normal'
    stavka01['state'] = 'readonly'
    stavka02['state'] = 'readonly'
    stavka03['state'] = 'readonly'
    stavka04['state'] = 'readonly'
    stavka01.current(0)
    stavka02.current(0)
    stavka03.current(0)
    stavka04.current(0)

    x01 = 20
    x02 = 20
    x03 = 20
    x04 = 20
    horsePlaceInWindow()

    refresh_combo(event_object='')
    view_weather()
    health_horse()
    insertText(f'Ваши средства: {int(money)} {valuta}.')

    if money < 1:
        messagebox.showinfo('Стоп!', 'На иммопдром без средств заходить нельзя!')
        quit(0)

def problem_horse():
    global reverse01, reverse02, reverse03, reverse04
    global play01, play02, play03, play04
    global fast_speed01, fast_speed02, fast_speed03, fast_speed04

    horse = randint(1, 4)
    max_rand = 10000

    if horse == 1 and play01 == True and x01 > 0:
        if randint(0, max_rand) < state01 * 5:
            reverse01 = not reverse01
            messagebox.showinfo('АааААааАаа!', f'Лошадь {nameHorse01} развернулась и бежит в другую сторону!')
        elif randint(0, max_rand) < state01 * 5:
            play01 = False
            messagebox.showinfo('Никогда такого не былои вот опять', f'{nameHorse01} заржала и скинула жокея!')
        elif randint(0, max_rand) < state01 * 5 and not fast_speed01:
            fast_speed01 = True
            messagebox.showinfo('Великолепно!', f'{nameHorse01} перестала притворяться и ускорилась!')
    elif horse == 2 and play02 == True and x02 > 0:
        if randint(0, max_rand) < state02 * 5:
            reverse02 = not reverse02
            messagebox.showinfo('АааААааАаа!', f'Лошадь {nameHorse02} развернулась и бежит в другую сторону!')
        elif randint(0, max_rand) < state02 * 5:
            play02 = False
            messagebox.showinfo('Никогда такого не былои вот опять', f'{nameHorse02} заржала и скинула жокея!')
        elif randint(0, max_rand) < state02 * 5 and not fast_speed02:
            fast_speed02 = True
            messagebox.showinfo('Великолепно!', f'{nameHorse02} перестала притворяться и ускорилась!')
    elif horse == 3 and play03 == True and x03 > 0:
        if randint(0, max_rand) < state03 * 5:
            reverse03 = not reverse03
            messagebox.showinfo('АааААааАаа!', f'Лошадь {nameHorse03} развернулась и бежит в другую сторону!')
        elif randint(0, max_rand) < state03 * 5:
            play03 = False
            messagebox.showinfo('Никогда такого не былои вот опять', f'{nameHorse03} заржала и скинула жокея!')
        elif randint(0, max_rand) < state03 * 5 and not fast_speed03:
            fast_speed03 = True
            messagebox.showinfo('Великолепно!', f'{nameHorse03} перестала притворяться и ускорилась!')
    elif horse == 4 and play04 == True and x04 > 0:
        if randint(0, max_rand) < state04 * 5:
            reverse04 = not reverse04
            messagebox.showinfo('АааААааАаа!', f'Лошадь {nameHorse04} развернулась и бежит в другую сторону!')
        elif randint(0, max_rand) < state04 * 5:
            play04 = False
            messagebox.showinfo('Никогда такого не былои вот опять', f'{nameHorse04} заржала и скинула жокея!')
        elif randint(0, max_rand) < state04 * 5 and not fast_speed04:
            fast_speed04 = True
            messagebox.showinfo('Великолепно!', f'{nameHorse04} перестала притворяться и ускорилась!')

def move_horse():
    global x01, x02, x03, x04

    if randint(0, 100) < 20:
        problem_horse()

    speed01 = (randint(1, time_day + weather) + randint(1, int((7 - state01)) * 3)) / randint(10, 175)
    speed02 = (randint(1, time_day + weather) + randint(1, int((7 - state02)) * 3)) / randint(10, 175)
    speed03 = (randint(1, time_day + weather) + randint(1, int((7 - state03)) * 3)) / randint(10, 175)
    speed04 = (randint(1, time_day + weather) + randint(1, int((7 - state04)) * 3)) / randint(10, 175)

    multiple = 1.5
    speed01 *= int(randint(1, 2 + state01) * (1 + fast_speed01 * multiple))
    speed02 *= int(randint(1, 2 + state02) * (1 + fast_speed02 * multiple))
    speed03 *= int(randint(1, 2 + state03) * (1 + fast_speed03 * multiple))
    speed04 *= int(randint(1, 2 + state04) * (1 + fast_speed04 * multiple))

    if play01:
        if not reverse01:
            x01 += speed01
        else:
            x01 -= speed01
    if play02:
        if not reverse02:
            x02 += speed02
        else:
            x02 -= speed02
    if play03:
        if not reverse03:
            x03 += speed03
        else:
            x03 -= speed03
    if play04:
        if not reverse04:
            x04 += speed04
        else:
            x04 -= speed04

    horsePlaceInWindow()

    all_play = play01 or play02 or play03 or play04
    all_x = x01 < 0 and x02 < 0 and x03 < 0 and x04 < 0
    all_reverse = reverse01 and reverse02 and reverse03 and reverse04

    if not all_play or all_x or all_reverse:
        win_round(0)
        return 0

    if x01 < 952 and x02 < 952 and x03 < 952 and x04 < 952:
        root.after(5, move_horse)
    else:
        if x01 >= 952:
            win_round(1)
        elif x02 >= 952:
            win_round(2)
        elif x03 >= 952:
            win_round(3)
        elif x04 >= 952:
            win_round(4)


def run_horse():
    global money

    startButton['state'] = 'disabled'
    stavka01['state'] = 'disabled'
    stavka02['state'] = 'disabled'
    stavka03['state'] = 'disabled'
    stavka04['state'] = 'disabled'
    money -= summ01.get() + summ02.get() + summ03.get() + summ04.get()
    move_horse()

def refresh_combo(event_object):
    summ = summ01.get() + summ02.get() + summ03.get() + summ04.get()
    labelAllMoney['text'] = f"Осталось средств на счету: {int(money - summ)} {valuta}"

    stavka01['values'] = get_values(int(money - summ02.get() - summ03.get() - summ04.get()))
    stavka02['values'] = get_values(int(money - summ01.get() - summ03.get() - summ04.get()))
    stavka03['values'] = get_values(int(money - summ02.get() - summ01.get() - summ04.get()))
    stavka04['values'] = get_values(int(money - summ02.get() - summ03.get() - summ01.get()))

    if summ01.get() > 0:
        horse01Game.set(True)
    else:
        horse01Game.set(False)
    if summ02.get() > 0:
        horse02Game.set(True)
    else:
        horse02Game.set(False)
    if summ03.get() > 0:
        horse03Game.set(True)
    else:
        horse03Game.set(False)
    if summ04.get() > 0:
        horse04Game.set(True)
    else:
        horse04Game.set(False)

    if summ > 0:
        startButton['state'] = 'normal'
    else:
        startButton['state'] = 'disabled'

def get_values(summa):
    value = []
    if summa > 9:
        for i in range(0, 11):
            value.append(i * (int(summa) // 10))
    else:
        value.append(0)
        if summa > 0:
            value.append(summa)
    return value

def loadMoney():
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        m = defaultMoney
    return m

def saveMoney(moneyToSave):
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except:
        quit(0)

def insertText(s):
    textDiary.insert(INSERT, s + "\n")
    textDiary.see(END)

def view_weather():
    s = 'Сейчас на ипподроме '
    if time_day == 1:
        s += 'ночь, '
    elif time_day == 2:
        s += 'утро, '
    elif time_day == 3:
        s += 'день, '
    elif time_day == 4:
        s += 'вечер, '

    if weather == 1:
        s += 'льёт сильный дождь.'
    elif weather == 2:
        s += 'моросит дождик.'
    elif weather == 3:
        s += 'облачно, на горизонте тучи.'
    elif weather == 4:
        s += 'безоблачно, ветер.'
    elif weather == 5:
        s += 'безоблачно, прекрасная погода!'
    insertText(s)

def horsePlaceInWindow():
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x02), y=100)
    horse03.place(x=int(x03), y=180)
    horse04.place(x=int(x04), y=260)

def get_heals(name, state, win):
    s = f'Лошадь {name} '
    if state == 5:
        s += 'мучается нсварением желудка.'
    elif state == 4:
        s += 'плохо спала. Подёргивается веко.'
    elif state == 3:
        s += 'сурова и беспощадна.'
    elif state == 2:
        s += 'в отличном настроении, покушала хорошо.'
    elif state == 1:
        s += 'просто ракета!'

    s += f' ({win}:1)'
    return s

def health_horse():
    insertText(get_heals(nameHorse01, state01, win_coef01))
    insertText(get_heals(nameHorse02, state02, win_coef02))
    insertText(get_heals(nameHorse03, state03, win_coef03))
    insertText(get_heals(nameHorse04, state04, win_coef04))

# ====================================================================

root = Tk()

# ********************************************************************
# ПЕРЕМЕННЫЕ
# ********************************************************************
WIDTH = 1024
HEIGHT = 600

x01 = 20
x02 = 20
x03 = 20
x04 = 20
nameHorse01 = "Ананас"
nameHorse02 = "Сталкер"
nameHorse03 = "Прожорливый"
nameHorse04 = "Копытце"

defaultMoney = 10000
money = 0
valuta = "$"

# ====================================================================

# ********************************************************************
# ФОРМИРОВАНИЕ ЭЛЕМЕНТОВ В ОКНЕ
# ********************************************************************
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POX_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

root.title("ИППОДРОМ")
root.resizable(False, False)
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POX_Y}")

road_image = PhotoImage(file="road.png")
road = Label(root, image=road_image)
road.place(x=0, y=17)

root.iconbitmap("hico.ico")

horse01_image = PhotoImage(file="horse01.png")
horse01 = Label(root, image=horse01_image)
horse02_image = PhotoImage(file="horse02.png")
horse02 = Label(root, image=horse02_image)
horse03_image = PhotoImage(file="horse03.png")
horse03 = Label(root, image=horse03_image)
horse04_image = PhotoImage(file="horse04.png")
horse04 = Label(root, image=horse04_image)
horsePlaceInWindow()

startButton = Button(text="СТАРТ", font="arial 20", width=61, background="#37AA37")
startButton.place(x=20, y=370)
startButton['state'] = 'disabled'

textDiary = Text(width=70, height=8, wrap=WORD)
textDiary.place(x=430, y=450)

scroll = Scrollbar(command=textDiary.yview, width=20)
scroll.place(x=993, y=450, height=132)
textDiary["yscrollcommand"] = scroll.set

money = loadMoney()

if money <= 0:
    messagebox.showinfo("Стоп!", "На ипподром без средств заходить нельзя!")
    quit(0)

labelAllMoney = Label(text=f"Осталось средств на счету: {money} {valuta}", font="arial 12")
labelAllMoney.place(x=20, y=565)

labelHorse01 = Label(text="Ставка на лошадь №1")
labelHorse01.place(x=20, y=450)
labelHorse02 = Label(text="Ставка на лошадь №2")
labelHorse02.place(x=20, y=480)
labelHorse03 = Label(text="Ставка на лошадь №3")
labelHorse03.place(x=20, y=510)
labelHorse04 = Label(text="Ставка на лошадь №4")
labelHorse04.place(x=20, y=540)

horse01Game = BooleanVar()
horse01Game.set(0)
horseCheck01 = Checkbutton(text=nameHorse01, variable=horse01Game, onvalue=1, offvalue=0)
horseCheck01.place(x=150, y=448)
horse02Game = BooleanVar()
horse02Game.set(0)
horseCheck02 = Checkbutton(text=nameHorse02, variable=horse02Game, onvalue=1, offvalue=0)
horseCheck02.place(x=150, y=478)
horse03Game = BooleanVar()
horse03Game.set(0)
horseCheck03 = Checkbutton(text=nameHorse03, variable=horse03Game, onvalue=1, offvalue=0)
horseCheck03.place(x=150, y=508)
horse04Game = BooleanVar()
horse04Game.set(0)
horseCheck04 = Checkbutton(text=nameHorse04, variable=horse04Game, onvalue=1, offvalue=0)
horseCheck04.place(x=150, y=538)

horseCheck01['state'] = 'disabled'
horseCheck02['state'] = 'disabled'
horseCheck03['state'] = 'disabled'
horseCheck04['state'] = 'disabled'

stavka01 = ttk.Combobox(root)
stavka02 = ttk.Combobox(root)
stavka03 = ttk.Combobox(root)
stavka04 = ttk.Combobox(root)

stavka01["state"] = "readonly"
stavka01.place(x=280, y=450)
stavka02["state"] = "readonly"
stavka02.place(x=280, y=480)
stavka03["state"] = "readonly"
stavka03.place(x=280, y=510)
stavka04["state"] = "readonly"
stavka04.place(x=280, y=540)

summ01 = IntVar()
summ02 = IntVar()
summ03 = IntVar()
summ04 = IntVar()

stavka01['textvariable'] = summ01
stavka02['textvariable'] = summ02
stavka03['textvariable'] = summ03
stavka04['textvariable'] = summ04

stavka01.bind('<<ComboboxSelected>>', refresh_combo)
stavka02.bind('<<ComboboxSelected>>', refresh_combo)
stavka03.bind('<<ComboboxSelected>>', refresh_combo)
stavka04.bind('<<ComboboxSelected>>', refresh_combo)
refresh_combo('')

stavka01.current(0)
stavka02.current(0)
stavka03.current(0)
stavka04.current(0)

setup_horse()
view_weather()
health_horse()
startButton['command'] = run_horse
# ====================================================================

root.mainloop()