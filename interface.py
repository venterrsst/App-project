from tkinter import *
from pygame import mixer
import game_crocodile as game
root = Tk()
window2 = None
window3 = None
entry = None
hints = None
button_repeat = None
background_game = None
canvas_window = None
heart1 = None
heart2 = None
heart3 = None
heart = None
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
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)
    except:
        pass

def stop_music():
    mixer.music.stop()

def play_music_game():
    try:
        mixer.music.load(music_game)
        mixer.music.set_volume(0.1)
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
    canvas_window.itemconfigure(hints, text=f"1 подсказка: {game.prompts[0]}")
    canvas_window.itemconfigure(heart1, state="normal")
    canvas_window.itemconfigure(heart2, state="normal")
    canvas_window.itemconfigure(heart3, state="normal")
    button_repeat.place_forget()

def open_window(event):
    stop_music()
    play_music_game()
    root.withdraw()
    global window2, entry, hints, button_repeat, background_game, ROOT_HEIGHT, ROOT_WIDTH
    global heart1, heart2, heart3, canvas_window, heart
    game.log("Пользователь начал игру")
    window2 = Toplevel(root)
    window2.attributes("-fullscreen", True)
    background_game = PhotoImage(file="background_game.png")
    canvas_window = Canvas(window2, width=3000, height=1500, bg="lightblue")
    canvas_window.background_game = background_game
    canvas_window.create_image(0, 0, image=canvas_window.background_game, anchor="nw")
    canvas_window.create_text(140, 30, text="Счетчик:", font=("Arial", 44, "bold"), fill="black")
    # canvas_window.create_text(120, 100, text=f"{game.attempts_left}", font=("Arial", 36, "bold"), fill="red")
    hints = canvas_window.create_text(ROOT_WIDTH//2-10, ROOT_HEIGHT//3-40, text=f"1 подсказка: {game.prompts[0]}", font=("Arial", 20), fill="black")
    heart = PhotoImage(file="heart.png")
    heart1 = canvas_window.create_image(50, 100, image=heart)
    heart2 = canvas_window.create_image(150, 100, image=heart)
    heart3 = canvas_window.create_image(250, 100, image=heart)
    canvas_window.place(x=0, y=0)
    entry = Entry(window2, font=("Arial", 18), width=30)
    entry.place(x=ROOT_WIDTH//2-200, y=ROOT_HEIGHT//3)
    ok = Button(window2, text="OK", font=("Arial", 14, "bold"), width=2, height=1, command=check_word, bg="green", fg="white")
    ok.place(x=ROOT_WIDTH//2+200, y=ROOT_HEIGHT//3-5)
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
    description = Label(window3, text="Крокодил представляет собой однопользовательскую программу,\
 генерирующую рандомные слова, которые игрок должен угадать по ассоциациям.\
 Всего дается 3 попытки. Каждая следующая попытка добавляет новую ассоциацию\
 к слову. Игра заканчивается, когда игрок угадывает загаданное слово, или когда\
 заканчивается количество попыток.", font=("Arial", 20), bg="lightblue",\
        fg="black", justify="left", wraplength=ROOT_WIDTH-50)
    description.pack(pady=50)
    button4 = Button(window3, text="Вернуться в меню", font=("Arial", 18, "bold"), width=20, height=2, bg="white", fg="black")
    button4.bind("<Button-1>", back_to_main_window2)
    button4.pack(pady=50)

def check_word():
    information = entry.get()
    game.log(f"Пользователь ввел слово {information}")
    if the_word.strip().lower() == information.strip().lower():
        canvas_window.itemconfigure(hints, text="Угадали!")
        game.log("Пользователь угадал слово")
        entry.delete(0, END)
        button_repeat.place(relx=0.5, rely=0.45, anchor="center")
    elif game.attempts_left == 3:
        game.attempts_left -= 1
        canvas_window.itemconfigure(heart3, state="hidden")
        canvas_window.itemconfigure(hints, text=f"2 подсказка: {game.prompts[1]}")
    elif game.attempts_left == 2:
        game.attempts_left -= 1
        canvas_window.itemconfigure(heart2, state="hidden")
        canvas_window.itemconfigure(hints, text=f"3 подсказка: {game.prompts[2]}")
    else:
        game.attempts_left -= 1
        canvas_window.itemconfigure(heart1, state="hidden")
        canvas_window.itemconfigure(hints, text=f"Не угадали! Правильное слово: {the_word}")
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