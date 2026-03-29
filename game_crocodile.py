import random
import json
with open("data.json", encoding="utf-8") as f:
    WORDS = json.load(f)
'''WORDS = {
    "тостер": ["кухня", "завтрак", "хлеб"],
    "аквариум": ["рыбки", "вода", "стекло"],
    "гитара": ["струны", "музыка", "аккорды"],
    "пылесос": ["уборка", "пыль", "шум"],
    "календарь": ["даты", "месяцы", "праздники"],
    "самолет": ["небо", "крылья", "аэропорт"],
}'''
key, prompts, attempts_left, count_prompts = 0, [""], 0, 0
def start():
    global key, prompts, attempts_left, count_prompts
    wordprompts = random.choice(WORDS)
    key = wordprompts["word"]
    prompts = wordprompts["prompts"]
    attempts_left = 3
    count_prompts = 1

def log(info):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(str(info)+"\n")
# print("Игра «Крокодил».")
# print("У вас", attempts_left, "попыток(и).")

'''while attempts_left > 0:
    # print("\nПодсказки:", ", ".join(hints[:count_hints]))
    guess = input("Ваш ответ: ")
    guess = guess.strip().lower()

    if guess == key:
        # print("Верно! Загаданное слово:", key)
        exit()

    attempts_left -= 1
    # print("Не угадали. Осталось попыток:", attempts_left)
    count_hints += 1

# print("\nПопытки закончились.")
# print("Загаданное слово было:", key)'''