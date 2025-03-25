# /games/__init__.py
# Инициализация пакета games и определение доступных игр
from .lcm_game import get_lcm_game_data
from .progression_game import get_progression_game_data

GAMES = {
    "1": ("Find the smallest common multiple of given numbers.",
          get_lcm_game_data),
    "2": ("What number is missing in the progression?",
          get_progression_game_data),
}
