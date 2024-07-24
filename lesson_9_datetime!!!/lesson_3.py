# Создаем список my_list2
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]

# Создаем пустой список new_list2
new_list2 = []
# Проходимся по каждому элементу в my_list2
for x in my_list2:
    if x % 2 == 0:  # Проверяем, является ли элемент четным
        new_list2.append(x)  # Если да, добавляем его в new_list2

print(new_list2)  # Выводим список new_list2


# Создаем список my_list2
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]

# Определяем функцию is_even, которая возвращает True, если x четное
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

# Используем функцию filter с функцией is_even для фильтрации четных чисел из my_list2
new_list2 = filter(is_even, my_list2)
print(list(new_list2))  # Преобразуем результат в список и выводим его


# Создаем список my_list4
my_list4 = [1, 2, 3, 4, 5, 6, 7, 8]

# Определяем функцию is_even, которая возвращает True, если x четное
def is_even(x):
    return x % 2 == 0

# Используем функцию filter с функцией is_even для фильтрации четных чисел из my_list4
new_list4 = filter(is_even, my_list4)
print(list(new_list4))  # Преобразуем результат в список и выводим его


# Создаем список my_list2
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]

# Используем функцию filter с лямбда-функцией для фильтрации четных чисел из my_list2
new_list2 = filter(lambda x: x % 2 == 0, my_list2)  # лямбда-функция проверяет, является ли число четным
print(list(new_list2))  # Преобразуем результат в список и выводим его
