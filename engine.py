# engine.py
# Основной движок игры: запускает выбранную игру и управляет процессом

def run_game(get_game_data, game_rule):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_rule)  # Вывод правил игры

    rounds = 3  # Количество раундов
    for _ in range(rounds):
        question, correct_answer = get_game_data()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при первой ошибке

    print(f"Congratulations, {name}!")
