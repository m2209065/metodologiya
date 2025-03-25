# main.py
# Главный файл: предоставляет пользователю выбор игры и запускает её
from engine import run_game
from games import GAMES


def main():
    print("Welcome to the Brain Games!")
    print("Please select a game to play:")

    for key, (description, _) in GAMES.items():
        print(f"'{key}' to choose {description}")

    choice = input("Your choice: ")

    if choice in GAMES:
        game_rule, get_game_data = GAMES[choice]
        run_game(get_game_data, game_rule)
    else:
        print("Invalid choice. Please select a valid game number.")


if __name__ == "__main__":
    main()
