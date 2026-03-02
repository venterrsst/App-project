import random

WORDS = {
    "тостер": ["кухня", "завтрак", "хлеб"],
    "аквариум": ["рыбки", "вода", "стекло"],
    "гитара": ["струны", "музыка", "аккорды"],
    "пылесос": ["уборка", "пыль", "шум"],
    "календарь": ["даты", "месяцы", "праздники"],
    "самолет": ["небо", "крылья", "аэропорт"],
}

key, hints = random.choice(list(WORDS.items()))
attempts_left = 3
count_hints = 1

print("Игра «Крокодил».")
print("У вас", attempts_left, "попыток(и).")

while attempts_left > 0:
    print("\nПодсказки:", ", ".join(hints[:count_hints]))
    guess = input("Ваш ответ: ")
    guess = guess.strip().lower()

    if guess == key:
        print("Верно! Загаданное слово:", key)
        exit()

    attempts_left -= 1
    print("Не угадали. Осталось попыток:", attempts_left)
    count_hints += 1

print("\nПопытки закончились.")
print("Загаданное слово было:", key)