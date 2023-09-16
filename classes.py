class BasicWord:
    """
    Класс для определения изначального слова
    и слов которые из него можно составить.
    """

    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

    def check_in_sub_words(self, check_word):
        # Проверка наличия слова в списке подслов
        if check_word in self.sub_words:
            return True
        return False

    def count_sub_words(self):
        # Возвращает количество подслов
        return len(self.sub_words)

    def get_min_len(self):
        # Возвращает минимальную длину подслова
        return len(min(self.sub_words))

    def print_word(self):
        # Возвращает изначальное слово
        return self.word

    def __repr__(self):
        return f"BasicWord({self.word}, {self.sub_words})"

    def __str__(self):
        return self.word


class Player:
    """
    Класс определения нового игрока,
    где будут сохраняться использованные им слова.
    """
    def __init__(self, name_player, used_sub_words=None):
        # Инициализация объекта игрока
        self.name = name_player
        self.used_sub_words = used_sub_words or []

    def get_count_used_words(self):
        # Возвращает количество использованных слов
        return len(self.used_sub_words)

    def write_used_word(self, sub_word):
        # Записывает использованное подслово
        self.used_sub_words.append(sub_word)

    def check_word_is_used(self, word):
        # Проверяет, было ли слово использовано игроком
        if word in self.used_sub_words:
            return True
        return False

    def __repr__(self):
        return f"Player({self.name}, {self.used_sub_words})"
