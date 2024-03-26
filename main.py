from game import generate_number, check_guess, welcome_message, prompt_message, error_message, success_message
from colorama import init, Fore, Style

def main():
    init(autoreset=True)  # автоматически сбрасывать цвет после каждого вывода
    secret_number = generate_number()
    attempts = 0

    print(welcome_message())

    print(Fore.YELLOW + "Я загадал число от 1 до 100. Попробуйте угадать." + Style.RESET_ALL)  # желтый цвет

    while True:
        try:
            guess = int(input(prompt_message()))
            attempts += 1
            result = check_guess(secret_number, guess)
            print(result)

            if "Поздравляю" in result:
                print(success_message(attempts))
                break

        except ValueError:
            print(error_message())

if __name__ == "__main__":
    main()
