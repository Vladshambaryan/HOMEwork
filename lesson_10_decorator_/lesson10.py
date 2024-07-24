# def calc():
#     print(1 + 1)
#
# calc()
# print(calc)
# new_calc = calc
# print(new_calc)
# new_calc()
# a = 1
#
# #@@@@@@@@@@@@@@@@@@@@@@
#
# def greet():
#     def hello():
#         return 'hellllllo'
#
#     return hello()
#
# print(greet())
#
# #@@@@@@@@@@@@@@@@@@@@@@@
# def outer():
#
#     def inner():
#         result = 2 + 5
#         return result
#
#     return inner
#
#
# print(outer()())
# inner = outer()
# print(inner())

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
# def madin1(give_me_a_func):
#     print('before')
#     give_me_a_func()
#     print('after')
#
# def model1():
#     print('mers1')
#
# def model2():
#     print('bmw2')
#
# model1()
# model2()
#
# madin1(model1)
# madin1(model2)
#
# def simple3():
#     print('I')
#     print('love')
#     print('Python')
#     print('and')
#     print('decorators')
# madin1(simple3)
# #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def add_text(func):
#     def wrapper():
#         print('before')
#         func()
#         print('after')
#
#     return wrapper
#
#
# def simple1():
#     print('simple1')
#
#
# simple1()
#
# simple1 = add_text(simple1)
#
# print(simple1)
# simple1()
#
#
# def simple2():
#     print('simple2')
#
#
# simple2()
#
# simple2 = add_text(simple2)
#
# simple2()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#
# def add_text(func):
#
#     def wrapper():
#         print('before')
#         func()
#         print('after')
#
#     return wrapper
#
#
# @add_text
# def simple1():
#     print('simple1')
#
# @add_text
# def simple2():
#     print('simple2')
#
# simple1()
# simple2()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def add_logs(func):
#     def wrapper():
#         print(f'function {func.__name__} started')
#         result = func()
#         print(f'finished {func.__name__}')
#         return result
#
#     return wrapper
#
#
# @add_logs
# def read():
#     print('read')
#
#
# @add_logs
# def read_logs2():
#     print('read logs')
#     print('read logs')
#
#
# @add_logs
# def print_nothing():
#     return 'hello'
#
#
# @add_logs
# def calc(x):
#     print(x * 2)
#
#
# read()
# read_logs2()
# print(print_nothing())
#
#
# def add_logs(func):
#     def wrapper(*args):
#         print(f'function {func.__name__} started')
#         result = func(*args)
#         print(f'finished {func.__name__}')
#         return result
#
#     return wrapper
#
#
# @add_logs
# def simple1():
#     print('simple1')
#
#
# @add_logs
# def print_nothing():
#     return 'hello'
#
#
# @add_logs
# def calc(x):
#     print(x * 2)
#
#
# @add_logs
# def calc2(x, y):
#     print(x * y)
#
#
# # simple1()
# # print(print_nothing())
# calc(3)
# calc2(3, 7)
#

def separator():
    print('=' * 20)
separator()

def func(*args):
    # print((1, 2, 3, 5, 9))
    print(*args)
    # print(1, 2, 3, 5, 9)

func(1, 2, 3, 5, 9)

def separator():
    print('=' * 20)
separator()

# Исходный список чисел
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

# Применение функции map с лямбда-функцией для удвоения каждого элемента в списке
new_list = map(lambda x: x * 2, my_list)

# Преобразование объекта map в список и его вывод
print(list(new_list))  # Вывод: [2, 4, 6, 8, 10, 12, 14, 16, 20]


def separator():
    print('=' * 20)
separator()

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

new_list = []
for x in my_list:
    if x % 2 == 0:
        new_list.append(x)

new_list = filter(lambda x: x % 2 == 0, my_list)
# new_list = [x for x in my_list if x % 2 == 0]
# new_list2 = [x if x % 2 == 0 else x + 1 for x in my_list]
# new_list2 = [x if x % 2 == 0 else print(f'{x} is not even') for x in my_list]
new_generator = (x for x in my_list if x % 2 == 0)

# print(new_list)
# print(new_list2)
print(list(new_list))
print(list(new_generator))


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

{1: 3, 'SDFSDF': 'WER'}

new_dict = {}
for x in my_list:
    new_dict[x] = x * 3

new_dict = {x: x * 3 for x in my_list}

print(new_dict)

def separator():
    print('=' * 20)
separator()
# Исходный список чисел
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]

# Использование генератора словаря для создания нового словаря
# Ключами являются элементы списка my_list, значениями — элементы, умноженные на 3
new_dict = {x: x * 3 for x in my_list}

# Вывод нового словаря
print(new_dict)

def separator():
    print('=' * 20)
separator()

data = [('one', 'two'), ('three', 'four')]

# new_dict = {}
# for key, value in data:
#     new_dict[key] = value

# new_dict = {key: value for key, value in data}
new_dict = dict(data)

print(new_dict)




# Исходный список кортежей
data = [('one', 'two'), ('three', 'four')]

# Преобразование списка кортежей в словарь
new_dict = dict(data)

# Вывод нового словаря
print(new_dict)

def separator():
    print('=' * 20)
separator()

countries = ['USA', 'Hawaii', 'Cuba']
temps = [23, 33, 35]

country_temps_dict = dict(zip(countries, temps))
print(country_temps_dict)

# Список стран
countries = ['USA', 'Hawaii', 'Cuba']

# Список температур
temps = [23, 33, 35]

# Использование функции zip для соединения двух списков и преобразование в словарь
country_temps_dict = dict(zip(countries, temps))

# Вывод словаря
print(country_temps_dict)

























