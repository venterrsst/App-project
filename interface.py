from tkinter import *
root = Tk()
window2 = None
window3 = None
hint = "Море"

def close_window(event):
    root.destroy()

def back_to_main_window(event):
    global window2
    window2.destroy()
    root.deiconify()

def back_to_main_window2(event):
    global window3
    window3.destroy()
    root.deiconify()

def open_window(event):
    root.withdraw()
    global window2
    global hint
    window2 = Toplevel(root)
    window2.attributes("-fullscreen", True)
    counter = Label(window2, text="Счетчик")
    attempts = Label(window2, text="3")
    counter.pack()
    attempts.pack()
    hints = Label(window2, text=f"1 подсказка: {hint} ")
    hints.pack()
    entry = Entry(window2)
    entry.pack()
    ok = Button(window2, text="OK")
    ok.pack()
    button3 = Button(window2, text="Выйти из игры")
    button3.bind("<Button-1>", back_to_main_window)
    button3.pack()

def game_description(event):
    root.withdraw
    global window3
    window3 = Toplevel(root)
    window3.attributes("-fullscreen", True)
    name = Label(window3, text="Описание игры")
    name.pack()
    description = Label(window3, text="Крокодил представляет собой однопользовательскую программу,\nгенерирующую рандомные слова, которые игрок должен угадать по ассоциациям.\nВсего дается 3 попытки. Каждая следующая попытка добавляет новую ассоциацию к слову.\nИгра заканчивается, когда игрок угадывает загаданное слово, или когда заканчивается количество попыток.")
    description.pack()
    button4 = Button(window3, text="Вернуться в меню")
    button4.bind("<Button-1>", back_to_main_window2)
    button4.pack()

root.attributes("-fullscreen", True)
canvas = Canvas(root, width=3000, height=1500, bg="lightblue")
canvas.create_text(760, 40, text="Крокодил", font=("Arial, 24"))
button1 = Button(root, text="Начать игру")
button5 = Button(root, text="Описание игры")
button2 = Button(root, text="Выйти из игры")
button2.bind("<Button-1>", close_window)
button1.bind("<Button-1>", open_window)
button5.bind("<Button-1>", game_description)
button1.place(x=20, y=60)
button5.place(x=20, y=80)
button2.place(x=20, y=100)
canvas.place(x=0, y=0)
root.mainloop()