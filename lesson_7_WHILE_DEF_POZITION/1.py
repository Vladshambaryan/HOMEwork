# Присваивает переменной `text` строку текста
text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris.'

words = text.split()  # Разбивает строку `text` на список слов
fin_words = []  # Создает пустой список для слов без 'o'
for word in words:  # Начинает цикл по каждому слову в списке `words`
    if word == 'end':  # Если слово равно 'end', прерывает цикл
        break
    elif 'o' in word:  # Если в слове содержится буква 'o', печатает слово и продолжает цикл
        print(word)
        continue
    fin_words.append(word)  # Если слово не содержит 'o', добавляет его в список `fin_words`
print(' '.join(fin_words))  # Объединяет все слова в списке `fin_words` обратно в строку и выводит её

