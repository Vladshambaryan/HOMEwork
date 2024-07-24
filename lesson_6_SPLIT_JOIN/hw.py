# Исходный текст
text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

# Разбиваем текст на слова с сохранением знаков препинания
words = text.split()

# Создаем список для преобразованных слов
new_words = []

# Проходим по каждому слову
for word in words:
    if word[-1] in ',.':  # Проверяем, если слово заканчивается на запятую или точку
        new_word = word[:-1] + 'ing' + word[-1]  # Добавляем 'ing' перед знаком препинания
    else:
        new_word = word + 'ing'  # Просто добавляем 'ing' к слову
    new_words.append(new_word)  # Добавляем новое слово в список

# Объединяем слова обратно в строку
new_text = ' '.join(new_words)

# Выводим результат
print(new_text)


# Перебираем числа от 1 до 100
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:  # Если число кратно и 3, и 5
        print("FuzzBuzz")
    elif i % 3 == 0:  # Если число кратно 3
        print("Fuzz")
    elif i % 5 == 0:  # Если число кратно 5
        print("Buzz")
    else:
        print(i)  # Если число не кратно ни 3, ни 5, выводим само число
