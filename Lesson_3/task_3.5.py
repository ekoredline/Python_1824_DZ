from random import choice


def joke(n):
    """ Фунуция возвращяет случайные шутки, сформированных из трех случайных слов, взятых из трёх списков. """

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    while n > 0:
        n -= 1
        print(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')


joke(30)
