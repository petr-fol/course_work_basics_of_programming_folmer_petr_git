from classes import Player
from utils import load_dict, load_random_word, word_is_good


def main():
    # Загрузка словаря
    words_dict = load_dict()
    # Получение случайного слова
    random_word = load_random_word(words_dict)

    # Ввод имени игрока
    player_name = input("Введите имя игрока\n")
    player = Player(player_name)
    # Получение минимальной длины подслова и общего количества подслов
    min_len = random_word.get_min_len()
    count = random_word.count_sub_words()
    word = random_word.print_word()

    print(f"Привет, {player_name}!")
    print(f"Составьте {count} слов из слова {word}")
    print(f"Слова должны быть не короче {min_len} букв")
    print(f'Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print(f"Поехали, ваше первое слово?")

    while True:
        player_word = input().lower()
        # Проверка корректности введенного слова игроком
        answer_for_player = word_is_good(player_word, player, random_word)

        if player.get_count_used_words() == count:
            break

        if answer_for_player not in [True, False]:
            print(answer_for_player)
            continue

        if answer_for_player:
            # Добавление использованного подслова игроком
            player.used_sub_words.append(player_word)
            print("верно")
            continue
        elif not answer_for_player:
            break

    print(f"Игра завершена, вы угадали {player.get_count_used_words()} слов!")


if __name__ == "__main__":
    main()
