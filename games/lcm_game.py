# /games/lcm_game.py
# Игра "НОК": вычисление наименьшего общего кратного трех чисел
import math
import random


def lcm(a, b, c):
    # Вычисляет наименьшее общее кратное (НОК) трех чисел
    return math.lcm(a, b, c)


def get_lcm_game_data():
    # Генерирует три случайных числа от 1 до 100
    numbers = [random.randint(1, 100) for _ in range(3)]
    question = " ".join(map(str, numbers))  # Формирование строки с вопросом
    correct_answer = str(lcm(*numbers))  # Вычисление правильного ответа
    return question, correct_answer
