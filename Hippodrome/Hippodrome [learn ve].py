from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# ********************************************************************
# МЕТОДЫ и ФУНКЦИИ
# ********************************************************************
def insertText(s):
    textDiary.insert(INSERT, s + "\n")
    textDiary.see(END)

def loadMoney():
    try:
        f = open("money.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует. Задано значение {defaultMoney} {valuta}.")
        m = defaultMoney
    return m

def saveMoney(moneyToSave):
    try:
        f = open("money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except:
        print("Ошибка создания файла! Наш Ипподром закрывается!")
        quit(0)

def horsePlaceInWindow():
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x02), y=100)
    horse03.place(x=int(x03), y=180)
    horse04.place(x=int(x04), y=260)
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
# ====================================================================

root.mainloop()
