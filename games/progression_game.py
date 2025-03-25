# /games/progression_game.py
# Игра "Геометрическая прогрессия": нахождение пропущенного элемента прогрессии
import random


def generate_progression():
    # Случайная длина прогрессии (от 5 до 10)
    length = random.randint(5, 10)
    # Начальный элемент прогрессии
    start = random.randint(1, 10)
    # Знаменатель прогрессии (множитель)
    ratio = random.randint(2, 5)
    # Генерация прогрессии
    progression = [start * (ratio ** i) for i in range(length)]

    # Выбор случайного элемента для скрытия
    hidden_index = random.randint(1, length - 2)
    # Запоминаем правильный ответ
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."  # Заменяем число на ".."

    # Формируем строку вопроса
    question = " ".join(map(str, progression))
    return question, correct_answer


def get_progression_game_data():
    return generate_progression()
