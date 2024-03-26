import random

def generate_number():
    return random.randint(1, 100)

def check_guess(secret_number, guess):
    if guess < secret_number:
        return "\033[91mЗагаданное число больше.\033[0m"  # красный цвет
    elif guess > secret_number:
        return "\033[91mЗагаданное число меньше.\033[0m"  # красный цвет
    else:
        return "\033[92mПоздравляю! Вы угадали число!\033[0m"  # зеленый цвет

def welcome_message():
    return "\033[96mДобро пожаловать в игру 'Угадай число'!\033[0m"  # цвет морской волны

def prompt_message():
    return "\033[93mВведите ваше предположение: \033[0m"  # желтый цвет

def error_message():
    return "\033[91mОшибка! Пожалуйста, введите целое число.\033[0m"  # красный цвет

def success_message(attempts):
    return f"\033[92mПоздравляем! Вы угадали число! Количество попыток: {attempts}\033[0m"  # зеленый цвет
