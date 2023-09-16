from classes import BasicWord
from stop_words import stop_words


def load_dict():
    """
    Загружает словарь слов из удаленного источника.

    Returns:
        dict: Словарь слов в формате JSON.
    """
    import requests
    response = requests.get("https://www.jsonkeeper.com/b/QUK8")
    return response.json()


def load_random_word(words_dict):
    """
    Выбирает случайное слово из словаря.

    Args:
        words_dict (list): Словарь слов.

    Returns:
        BasicWord: Объект BasicWord, представляющий случайное слово.
    """
    import random
    random_dict = random.choice(words_dict)
    random_word_ = random_dict['word']
    random_sub_words = random_dict['subwords']
    basic_word = BasicWord(random_word_, random_sub_words)
    return basic_word


def word_is_good(player_word, player, random_word):
    """
    Проверяет, является ли введенное слово корректным.

    Args:
        player_word (str): Введенное игроком слово.
        player (Player): Объект игрока.
        random_word (BasicWord): Случайное слово.

    Returns:
        Union[bool, str]: Результат проверки. Возвращает True, если слово корректно, False, если некорректно,
        или строку с объяснением, почему слово считается некорректным.
    """
    if player_word in stop_words:
        return False

    elif len(player_word) < 3:
        return "слишком короткое слово"

    elif player.check_word_is_used(player_word):
        return "уже использовано"

    elif player_word not in random_word.sub_words:
        return "неверно"

    elif player_word in random_word.sub_words:
        return True
