# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

numbers_translate = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(val):
    print(numbers_translate.get(val))


num_translate('one')
num_translate('two')
num_translate('three')
num_translate('four')
num_translate('five')
num_translate('six')
num_translate('seven')
num_translate('eight')
num_translate('nine')
num_translate('ten')
num_translate('eleven')