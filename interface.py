from tkinter import *
root = Tk()
window2 = None
hint = "Море"
def close_window(event):
    root.destroy()
def back_to_main_window(event):
    global window2
    window2.destroy()
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
root.attributes("-fullscreen", True)
label = Label(root, text="Крокодил")
button1 = Button(root, text="Начать игру")
button2 = Button(root, text="Выйти из игры")
button2.bind("<Button-1>", close_window)
button1.bind("<Button-1>", open_window)
label.pack()
button1.pack()
button2.pack()
root.mainloop()