from game import generate_number, check_guess

def main():
    secret_number = generate_number()
    attempts = 0

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте угадать.")

    while True:
        try:
            guess = int(input("Введите ваше предположение: "))
            attempts += 1
            result = check_guess(secret_number, guess)
            print(result)

            if result == "Поздравляю! Вы угадали число!":
                print(f"Количество попыток: {attempts}")
                break

        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()
