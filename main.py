# main.py
from game import generate_number, check_guess
from colorama import init, Fore, Style

def main():
    init(autoreset=True)  # автоматически сбрасывать цвет после каждого вывода
    secret_number = generate_number()
    attempts = 0

    print(Fore.CYAN + "Добро пожаловать в игру 'Угадай число'!" + Style.RESET_ALL)  # голубой цвет

    print(Fore.YELLOW + "Я загадал число от 1 до 100. Попробуйте угадать." + Style.RESET_ALL)  # желтый цвет

    while True:
        try:
            guess = int(input("Введите ваше предположение: "))
            attempts += 1
            result = check_guess(secret_number, guess)
            print(result)

            if "Поздравляю" in result:
                print(Fore.GREEN + f"Количество попыток: {attempts}" + Style.RESET_ALL)  # зеленый цвет
                break

        except ValueError:
            print(Fore.RED + "Ошибка! Пожалуйста, введите целое число." + Style.RESET_ALL)  # красный цвет

if __name__ == "__main__":
    main()
