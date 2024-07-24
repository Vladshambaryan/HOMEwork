# Пример функции с аргументами и значениями по умолчанию
def example(e, f, g, ff='one', gg='two'):
    print(e, f, g, ff, gg)

# Вызов функции с явным указанием значения аргумента gg
example(2, 3, 6, gg=444)
# Вызов функции с аргументами по умолчанию
example(3, 5, 7)
# Вывод: 2 3 6 one 444, 3 5 7 one two


# Пример функции с аргументом по умолчанию
def power(number, degree=2):
    return number ** degree

# Вызов функции с одним аргументом (используется значение по умолчанию)
print(power(2))
# Вызов функции с двумя аргументами
print(power(2, 3))
# Вывод: 4, 8

# Пример функции с позиционными аргументами
def print_words(first, second, third, fourth, fifth):
    print(f'The first word is {first}, second word is {second}, {third}, {fourth}, {fifth}')

# Вызов функции с позиционными аргументами
print_words('one', 'two', 'three', 'four', 'five')
# Вызов функции с именованными аргументами
print_words(fifth='five', third='three', fourth='four', first='one', second='two')
# Вывод: The first word is one, second word is two, three, four, five
