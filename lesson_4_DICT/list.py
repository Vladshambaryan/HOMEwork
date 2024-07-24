a = 1
a += 1
print(a)

a = 1
a -= 1
print(a)

text = "text"
# text = text + " new"
text += " new"
print(text)

symbol = "-"
symbol *= 30
print(symbol)
print('Copyrights')
print(symbol)

text = 'I love Python!'
print('love' in text)  # дублировать строку ctrl d
print('Love' in text)  # Операторы принадлежности

b = 256
print(id(b))
c = 256
print(id(c))
d = 257
print(id(d))
e = 257
print(id(e))
print(b is c) #Операторы идентичности
print(d is not e)

#user_name = input('What is your name?:')
#print('Hello', user_name, '!')

a = '1'
print(type(a))
a = int(a)
print(type(a))
a = str(a)
print(type(a))
b = 'True'
print(type(b))
b = bool(b)
print(type(b))
a = float(a)
print(type(a))
print(a)

# Number (целое число)
# String (строка)
# Boolean (логический тип данных)
# Float(числа с плавающей точкой)
# List (список) []
# Dictionary (словарь)
# Tuple (кортеж)  ()
# Set (множество) {}


my_list = [1, 3, 6, 7, None, 'text', False, 2.42, 'sdsdf', 'last', 'last2']
print(my_list[2])
print(my_list[-1]) #последний -1
print(my_list[-3])

my_list[2] = 42
print(my_list)

# my_list = []
# my_list = list()
my_list.append(42)  # добавить в конец списка
my_list.append('text')
print(my_list)

print(len(my_list))  #длинна списка

print(my_list.index('text'))  #индекс элемента text

poped = my_list.pop(0)  #delete

print(poped)

print("text" in my_list)













