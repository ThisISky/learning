from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests

# ********************************************************************
# МЕТОДЫ и ФУНКЦИИ
# ********************************************************************


# ********************************************************************
# ПЕРЕМЕННЫЕ
# ********************************************************************
root = Tk()
WIDTH = 604
HEIGHT = 604

# ********************************************************************
# ФОРМИРОВАНИЕ ЭЛЕМЕНТОВ В ОКНЕ
# ********************************************************************
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POX_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

root.title("Dodo Statistics")
root.resizable(False, False)
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POX_Y}")

back_image = PhotoImage(file="dodo_back.png")
back_photo = Label(root, image=back_image)
back_photo.place(x=0, y=0)

root.iconbitmap("favicon.ico")

label_сopyright = Label(text="Sky Dev @ 2020", font=["Comic Sans MS", 7], background="#D2691E")
label_сopyright.place(x=3, y=584)

label_ver = Label(text="ver 0.1", font=["Comic Sans MS", 7], background="#D2691E")
label_ver.place(x=567, y=584)

start_button = Button(text="Запуск", font=["Comic Sans MS", 15], width=15, background="#FF4500")
start_button.place(x=215, y=545)

label_domain = Label(text="Введите адрес группы:", font=["Comic Sans MS", 13], background="#F5DEB3")
label_domain.place(x=5, y=10)
txt_domain = Entry(width=15, font="Times 15")
txt_domain.grid(column=1, row=0)
txt_domain.place(x=5, y=45)

label_len_post = Label(text="Введите количество постов:", font=["Comic Sans MS", 13], background="#F5DEB3")
label_len_post.place(x=350, y=10)
txt_len_post = Entry(width=15, font="Times 15")
txt_len_post.grid(column=1, row=0)
txt_len_post.place(x=350, y=45)

root.mainloop()