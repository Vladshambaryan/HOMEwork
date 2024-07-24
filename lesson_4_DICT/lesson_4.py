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
symbol *= 30  # умножает символ - 30 раз
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
print(b is c)  # Операторы идентичности
print(d is not e)  # Операторы не идентичности

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
print(my_list[-1])  # последний -1
print(my_list[-3])  # последний -3

my_list[2] = 42
print(my_list)

# my_list = []
# my_list = list()
my_list.append(42)  # добавить в конец списка
my_list.append('text')
print(my_list)

print(len(my_list))  # длинна списка

print(my_list.index('text'))  # индекс элемента text

poped = my_list.pop(0)  # delete

print(poped)
print("text" in my_list)


# Tuple(кортежи)
my_tuple = (1, 3, 6, 7, None, 'text', False, 2.42)  # tuple неизменяемые
print(my_tuple[2])
print(my_tuple[-1])
print(my_tuple[-3])



# my_tuple = ()
# my_tuple = tuple()
my_tuple = (1, 5, 2, 6, 1)
print(my_tuple)
print(my_tuple.count(1)) #количество элемента 1 в этом кортедже
print(my_tuple.index(5)) #под каким индексом 5


llist = [56]
print(llist)
ttuple = (56,)  #запятая чтоб было понятно програме что это тюпл
print(ttuple)
print(type(ttuple))

# Set (множество)
my_set = {1, 3, 6, 7, None, 'text', False, 2.42, 3, 7}
# print(my_set[2])  # множество не индексируется
my_set.add(42)
my_set.add('text')
print(my_set)

list1 = list(set([1, 2, 5, 6, 2, 1, 8]))
list1 = set(list1)  # преобразование в set

list11 = list(set([1, 2, 5, 6, 2, 1, 8]))
list11= list(list1)  # преобразование в list

print(list1)
print(list11)

my_set = {} # Это словарь
print(type(my_set))
my_set = set() #  Пустой set можно создать только так
print(type(my_set))

# Dictionary (словарь)
my_dict = {'one': 'value', 'two': 'value2'}

print(my_dict['one'])
print(len(my_dict))  # длинна dict

my_dict['one'] = 'myvalue'  # изменение
my_dict['three'] = 'value3' #добавим чтото

my_dict['four'] = False  #добавим чтото
my_dict['five'] = [1, 5, 8]  #добавим список
my_dict['six'] = {1, 6, 9}  #добавим set

my_dict[2] = 'skldjflskdf'  # ключ может быть int
my_dict[False] = 'skdjhskdjf'  # ключ может быть bool
my_dict[2.42] = 'werwerw'  # ключ может быть float
my_dict[(1, 2)] = 'ieruyieurtert'  # ключ может быть tuple
my_dict[5] = {1: 2}  # ключ может быть словарь



print(my_dict)
print(type(my_dict))
#
print(my_dict.keys())  # получит все ключи
print(my_dict.values())  # получит все значения
print(my_dict.items())  # получит все ключи и значения








