import random
import json
with open("data.json", encoding="utf-8") as f:
    WORDS = json.load(f)

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