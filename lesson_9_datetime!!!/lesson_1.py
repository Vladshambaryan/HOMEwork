summer = True

# Проверяем, является ли переменная summer истиной
if summer is True:
    print('The weather is fine')  # Если да, выводим сообщение о хорошей погоде
else:
    print('The weather is not fine')  # Иначе, выводим сообщение о плохой погоде



import random  # Импортируем модуль random для работы со случайными числами
summer = random.choice([False, True])  # Присваиваем переменной summer случайное значение из списка [False, True]

# Проверяем, является ли переменная summer истиной
if summer:
    print('The weather is fine')  # Если да, выводим сообщение о хорошей погоде
else:
    print('The weather is not fine')  # Иначе, выводим сообщение о плохой погоде




a = 0

# Проверяем, не является ли переменная a None
if a is not None:
    print('...')  # Если не является, выводим '...'

numbers = [1, 45, 23, 67, 32, 89]  # Создаем список чисел
print(max(numbers))  # Выводим максимальное значение из списка

print(min(numbers))  # Выводим минимальное значение из списка
print(sum(numbers))  # Выводим сумму всех чисел в списке

a = 1 / 3
print(round(a, 2))  # Округляем значение переменной a до двух знаков после запятой

print(abs(1))  # Выводим абсолютное значение числа 1 (расстояние от нуля)

print(sorted(numbers))  # Выводим отсортированный по возрастанию список numbers
print(sorted(numbers, reverse=True))  # Выводим отсортированный по убыванию список numbers
print(numbers)  # Выводим оригинальный список numbers

numbers.sort()  # Сортируем список numbers по возрастанию
print(numbers)  # Выводим отсортированный список numbers

numbers.sort(reverse=True)  # Сортируем список numbers по убыванию
print(numbers)  # Выводим отсортированный список numbers

my_list = [1, 2, 3, 4, 5]  # Создаем список my_list

new_list = []
for x in my_list:
    new_list.append(x * 2)  # Умножаем каждый элемент списка my_list на 2 и добавляем в new_list

print(new_list)  # Выводим новый список new_list

my_list = [1, 2, 3, 4, 5]  # Создаем список my_list

def mult_by_2(x):
    return x * 2  # Функци


# a = input('Your name and surname : ').split()
# name, surname = a
# print(f'name is {name}, surname is {surname}')
#
# code, number = map(int, input('code and number : ').split())
# print(f'name is {code + 1}, surname is {number + 2}')









