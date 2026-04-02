from tkinter import *
from pygame import mixer
import game_crocodile as game
root = Tk()
window2 = None
window3 = None
entry = None
hints = None
attempts = None
button_repeat = None
WIDTH_BUTTON = 20
HEIGHT_BUTTON = 5
mixer.init()
music_menu = "music_menu.mp3"
music_game = "music_game.mp3"

game.start()
the_word = game.key

def play_menu():
    try:
        mixer.music.load(music_menu)
        mixer.music.play(-1)
    except:
        pass

def stop_music():
    mixer.music.stop()

def play_music_game():
    try:
        mixer.music.load(music_game)
        mixer.music.play(-1)
    except:
        pass

def close_window(event):
    stop_music()
    game.log("Пользователь вышел из игры")
    root.destroy()

def back_to_main_window(event):
    global window2
    stop_music()
    window2.destroy()
    root.deiconify()
    play_menu()

def back_to_main_window2(event):
    global window3
    window3.destroy()
    root.deiconify()

def repeat_game(event):
    global the_word
    game.start()
    the_word = game.key
    entry.delete(0, END)
    hints.config(text=f"1 подсказка: {game.prompts[0]}")
    attempts.config(text=f"{game.attempts_left}")
    button_repeat.place_forget()

def open_window(event):
    stop_music()
    play_music_game()
    root.withdraw()
    global window2, entry, hints, button_repeat, attempts
    game.log("Пользователь начал игру")
    window2 = Toplevel(root)
    window2.attributes("-fullscreen", True)
    window2.configure(bg="lightblue")
    background_game = Frame(window2, bg="lightblue")
    background_game.pack(fill=BOTH, expand=True)
    counter_frame = Frame(background_game, bg="lightblue")
    counter_frame.place(x=30, y=30)
    counter = Label(counter_frame, text="Счетчик:", font=("Arial", 44, "bold"), bg="lightblue", fg="black")
    counter.pack()
    attempts = Label(counter_frame, text=f"{game.attempts_left}", font=("Arial", 36, "bold"), bg="lightblue", fg="red")
    attempts.pack(pady=10)
    hints = Label(window2, text=f"1 подсказка: {game.prompts[0]}", font=("Arial", 20), bg="lightblue", fg="black", wraplength=800, justify="center")
    hints.place(relx=0.5, rely=0.3, anchor="center")
    entry_frame = Frame(window2, bg="lightblue")
    entry_frame.place(relx=0.5, rely=0.35, anchor="center")
    entry = Entry(entry_frame, font=("Arial", 18), width=30)
    entry.pack(side=LEFT, padx=10)
    ok = Button(entry_frame, text="OK", font=("Arial", 14, "bold"), width=2, height=1, command=check_word, bg="green", fg="white")
    ok.pack(side=LEFT, padx=0.1)
    button3 = Button(window2, text="Выйти из игры", font=("Arial", 16, "bold"), width=15, height=2, bg="red", fg="white")
    button3.bind("<Button-1>", back_to_main_window)
    button3.place(relx=0.95, rely=0.95, anchor="se")
    button_repeat = Button(window2, text="Начать снова", font=("Arial", 16, "bold"), width=15, height=2, bg="orange", fg="white")
    button_repeat.bind("<Button-1>", repeat_game)

def game_description(event):
    root.withdraw()
    global window3
    window3 = Toplevel(root)
    window3.attributes("-fullscreen", True)
    window3.configure(bg="lightblue")
    name = Label(window3, text="Описание игры", font=("Arial", 48, "bold"), bg="lightblue", fg="black")
    name.pack(pady=50)
    description = Label(window3, text="Крокодил представляет собой однопользовательскую программу,\nгенерирующую рандомные слова, которые игрок должен угадать по ассоциациям.\nВсего дается 3 попытки. Каждая следующая попытка добавляет новую ассоциацию к слову.\nИгра заканчивается, когда игрок угадывает загаданное слово, или когда заканчивается количество попыток.", font=("Arial", 20), bg="lightblue", fg="black", justify="center")
    description.pack(pady=50)
    button4 = Button(window3, text="Вернуться в меню", font=("Arial", 18, "bold"), width=20, height=2, bg="white", fg="black")
    button4.bind("<Button-1>", back_to_main_window2)
    button4.pack(pady=50)

def check_word():
    information = entry.get()
    game.log(f"Пользователь ввел слово {information}")
    if the_word.strip().lower() == information.strip().lower():
        hints.config(text="Угадали!")
        game.log("Пользователь угадал слово")
        entry.delete(0, END)
        button_repeat.place(relx=0.5, rely=0.45, anchor="center")
    elif game.attempts_left == 3:
        game.attempts_left -= 1
        attempts.config(text=f"{game.attempts_left}")
        hints.config(text=f"2 подсказка: {game.prompts[1]}")
    elif game.attempts_left == 2:
        game.attempts_left -= 1
        attempts.config(text=f"{game.attempts_left}")
        hints.config(text=f"3 подсказка: {game.prompts[2]}")
    else:
        game.attempts_left -= 1
        attempts.config(text=f"{game.attempts_left}")
        hints.config(text=f"Не угадали! Правильное слово: {the_word}")
        game.log("Пользователь проиграл")
        entry.delete(0, END)
        button_repeat.place(relx=0.5, rely=0.45, anchor="center")

root.attributes("-fullscreen", True)
root.update()
ROOT_WIDTH = root.winfo_width()
ROOT_HEIGHT = root.winfo_height()
game.log(f"Пользователь открыл окно с размером {ROOT_WIDTH}x{ROOT_HEIGHT}")
background_crocodile = PhotoImage(file="background_crocodile.png")
canvas = Canvas(root, width=3000, height=1500, bg="lightblue")
canvas.create_image(0, 0, image=background_crocodile, anchor="nw")
canvas.create_text(ROOT_WIDTH//2, 50, text="Крокодил", font=("Arial, 72"), fill="green")
button1 = Button(root, width=WIDTH_BUTTON, height=HEIGHT_BUTTON, text="Начать игру", font=("Arial", 9, "bold"), bg="white", fg="black")
button5 = Button(root, width=WIDTH_BUTTON, height=HEIGHT_BUTTON, text="Описание игры", font=("Arial", 9, "bold"), bg="white", fg="black")
button2 = Button(root, width=WIDTH_BUTTON, height=HEIGHT_BUTTON, text="Выйти из игры", font=("Arial", 9, "bold"), bg="white", fg="black")
button2.bind("<Button-1>", close_window)
button1.bind("<Button-1>", open_window)
button5.bind("<Button-1>", game_description)
button1.place(relx=0.5, rely=0.5, anchor="center")
button5.place(relx=0.5, rely=0.6, anchor="center")
button2.place(relx=0.5, rely=0.7, anchor="center")
canvas.place(x=0, y=0)
play_menu()
root.mainloop()