# Получает ввод от пользователя
user_input = input('your number: ')

# Проверяет, является ли ввод числом
if user_input.isnumeric():
    user_input = int(user_input)  # Преобразует ввод в целое число
    if user_input == 1:  # Если введенное число равно 1
        print('One')  # Печатает 'One'
    elif user_input == 2:  # Если введенное число равно 2
        print('two')  # Печатает 'two'
    elif user_input == 3:  # Если введенное число равно 3
        print('three')  # Печатает 'three'
    else:  # Иначе
        print('many')  # Печатает 'many'
else:
    print('Enter a number please')  # Печатает сообщение о неверном вводе

# Получает ввод от пользователя и сразу преобразует его в целое число
user_input = int(input('your number: '))

# Проверяет, является ли введенное число 1 и печатает 'One' при совпадении
if user_input == 1:
    print('One')

# Проверяет, является ли введенное число 2 и печатает 'two' при совпадении
if user_input == 2:
    print('two')

# Проверяет, является ли введенное число не 1 и не 2, и печатает 'many' при совпадении
if user_input not in [1, 2]:
    print('many')

# Проверяет, является ли введенное число больше 0
if user_input > 0:
    if user_input > 1:  # Если введенное число больше 1
        if user_input == 2:  # Если введенное число равно 2
            print()  # Печатает пустую строку
        elif user_input == 3:  # Если введенное число равно 3
            if 1 == 1:  # Если 1 равно 1 (что всегда истина)
                print()  # Печатает пустую строку
            elif 2 == 2:  # Если 2 равно 2 (что всегда истина)
                print()  # Печатает пустую строку
    elif 3 == 3:  # Если 3 равно 3 (что всегда истина)
        print()  # Печатает пустую строку

# Циклы

names = ['John', 'Tim', 'James', 'Bob', 'Jim', 'Bill']
print(names)  # Печатает весь список имен
print(names[0])  # Печатает первое имя в списке
print(names[1])  # Печатает второе имя в списке
print(names[2])  # Печатает третье имя в списке
print(names[3])  # Печатает четвертое имя в списке
print(names[4])  # Печатает пятое имя в списке

# Проходит по каждому имени в списке имен
for name in names:
    print(name)  # Печатает текущее имя
print('the end')  # Печатает 'the end' после завершения цикла


# Проходит по каждому имени в списке имен
names = ['John', 'Tim', 'James', 'Bob', 'Jim', 'Bill']

for name in names:  # Проходит по каждому имени в списке имен
    name = name.replace('i', 'I')  # Заменяет все 'i' в имени на 'I'
    if name.startswith('J'):  # Если имя начинается с 'J'
        print('Mr.', end=' ')  # Печатает 'Mr.' без новой строки
    print(name)  # Печатает текущее имя

# Проходит по каждому имени в кортежах имен
names = ('John', 'Tim', 'James', 'Bob', 'Jim', 'Bill')
for name in names:
    print(name)  # Печатает текущее имя

# Проходит по каждому имени в множестве имен
names = {'John', 'Tim', 'James', 'Bob', 'Jim', 'Bill'}
for name in names:
    print(name)  # Печатает текущее имя

# Словари
persons = {'John': 132, 'Tom': 167, 'James': 234}
print(persons.keys())  # Печатает все ключи словаря
for person in persons.keys():  # Проходит по каждому ключу в словаре
    print(person)  # Печатает текущий ключ

persons = {'John': 132, 'Tom': 167, 'James': 234}
print(persons.values())  # Печатает все значения словаря
for person in persons.values():  # Проходит по каждому значению в словаре
    print(person)  # Печатает текущее значение

persons = {'John': 132, 'Tom': 167, 'James': 234}
for person in persons:  # Проходит по каждому ключу в словаре
    print(f'{person}: {persons[person]}')  # Печатает ключ и его значение

persons = {'John': 132, 'Tom': 167, 'James': 234}
for name, height in persons.items():  # Проходит по каждому ключу и значению в словаре
    print(f'{name}: {height}')  # Печатает ключ и его значение

# Текст
text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris.'  # Присваивает переменной text строку текста
words = text.split()  # Разбивает строку text на список слов
fin_words = []  # Создает пустой список для слов без 'o'
for word in words:
    if 'o' in word:  # Если слово содержит 'o'
        print(word)  # Печатает слово
    else:
        fin_words.append(word)  # Если слово не содержит 'o', добавляет его в список fin_words
print(' '.join(fin_words))  # Объединяет все слова в списке fin_words обратно в строку и выводит её
