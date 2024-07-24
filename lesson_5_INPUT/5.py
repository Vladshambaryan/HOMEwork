[7]
my_list = [1, 3]
my_tuple = (2, 6, 9)
# a = my_list[0]
# b = my_list[1]  # дурной тон
# c = my_tuple[0]
# d = my_tuple[1]
# e = my_tuple[2]
a, b = my_list
c, d, e = my_tuple
print(a, b, c, d, e)

# срезы
lll = [1, 3, 5, 2, 5, 7 ,1, 3]
print(lll)
print(lll[1:4])
print(lll[:4])  # с 0 до 4
print(lll[3:]) # с 3 до конца
print(lll[1::2])  # с 1 до конца шаг 2
print(lll[:])  # с 0 до конца
print(lll[::-1])  # с конца до начала шаг 1
print(lll[::-2])  # с конца до начала шаг 2
print(lll[-2:-6:-1])  # с -2 до -6 шаг -1

# Методы строк

text = 'my long long integer'
print(text[3])
print(len(text))  # количества
print(text.index('long'))  # с какого индекса начинается слово лонг
print('long' in text)  # есть ли лонг в тексте
print(text.count('n'))  # количество букв n
print(text.count('long'))
print(text.find('lone'))  # не существующее слово
print(text[:7])  # первые 7 символов
print(text.startswith('my'))  # если текст начинается с my
print(text.endswith('integer'))  # если текст  заканчивается  словом integer

result1 = "результат операции: 42"
result2 = "результат операции: 514"
result3 = "результат работы программы: 9"

number1 = int(result1[result1.index(':') + 2:]) + 10  # находит индекс символа :  пропуская двоеточие и пробел
number2 = int(result2[result2.index(':') + 2:]) + 10
number3 = int(result3[result3.index(':') + 2:]) + 10

print(number1)
print(number2)
print(number3)

txt = "ThIs tExt wiTh meSsEd uP CaPITalIZatiOn!"
print(txt.capitalize()) # Делает первую букву предложения заглавной
print(txt.title())  # Делает каждую первую букву заглавной
print(txt.upper())  # Делает все буквы большими
print(txt.lower())  # Делает все буквы маленькими

text = 'mY lOng loNg STRING'
string_index = text.lower().index('string')  # находим где находится слово srtring и переводим в нижний регистр
print(text[:string_index].lower() + text[string_index:].upper())  # с начала до string_index печать lower + начиная с strring_index upper

# ПЕРЕДЕЛЫВАЕМ
msg = 'Hello world!'
msg = msg.replace('world', 'universe')  # старое меняем на новое
print(msg)

data = '12,3'
data = data.replace(',', '.')  # заменить , на .
print(data)


txt = '  admin  '
txt = txt.replace(' ', '')  # заменить пробел на ничего
txt = txt.strip()  # снять лишнее
txt = txt.lstrip()  # снять с лева
txt = txt.rstrip()  # снять  с права
print(txt)
text = '"(name)"'
text = text.strip('"()')  # почистить строку от этих символов
print(text)

#Строка ←→ список

my_string = 'some little text'
my_string2 = 'some,little,text'
list_from_text = my_string.split()  # разделить текст
list_from_text2 = my_string2.split(',')  # разделить текст ,
print(list_from_text)
print(list_from_text2)

languag = ['Python', 'Java', 'Ruby']
print(languag)
languag = ', '.join(languag)  # ставит запятые в середине
print(languag)

languages = ['Python', 'Java', 'Ruby']
print('Student knows these languages:', ', '.join(languages))  # переделывает в строку


# Форматирование строки

a = 'one'
b = 'two'
print('First word is', a, ', second word is', b)  # канкатенация

my_text = 'First word is ' + a + ', second word is ' + b  # канкатенация
print(my_text)

my_text = 'First word is %s, second word is %s'  # канкатенация
print(my_text % (a, b))

#string format
my_text = 'First word is {}, second word is {}'  # канкатенация
print(my_text.format(a, b))

my_text = 'First word is {1}, second word is {0}'  # канкатенация указываем куда вставить
print(my_text.format(a, b))


#f-string
a = 'five'
b = 'tree'
my_text = f'First word is {a}, second word is {b}'  # f string
print(my_text)


# template = 'Hello, {0}!'
username = input('What is your name?: ')  # пастановка
print(f'Hello, {username}!')
# print(template.format(username))

a = 'BMW'
b = 'AUDI'
my_text = 'First CAR is {}, second CAR is {}'  # пастановка
print_text = my_text.format(a, b)
print(print_text)
