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






















