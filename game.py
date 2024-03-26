import random

def generate_number():
    return random.randint(1, 100)

def check_guess(secret_number, guess):
    if guess < secret_number:
        return "Загаданное число больше."
    elif guess > secret_number:
        return "Загаданное число меньше."
    else:
        return "Поздравляю! Вы угадали число!"
    