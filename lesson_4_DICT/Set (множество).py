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