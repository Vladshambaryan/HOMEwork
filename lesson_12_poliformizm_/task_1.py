import json  # Импортируем модуль json для работы с JSON-файлами

# Функция для чтения данных из файла и возврата их в виде словаря
def read_file(filename):
    # Открываем файл с именем filename в режиме чтения ('r')
    with open(filename, 'r') as file_data:
        # Загружаем данные из файла в формате JSON
        data = json.load(file_data)
    # Возвращаем считанные данные
    return data

# Читаем данные из файла 'data1.txt' и сохраняем их в переменной data1
data1 = read_file('data/data1.txt')
# Читаем данные из файла 'data2.txt' и сохраняем их в переменной data2
data2 = read_file('data/data2.txt')

# Печатаем значение по ключу 'Country' из словаря data1
print(data1['Country'])
# Печатаем значение по ключу 'avg_temp' из словаря data1
print(data1['avg_temp'])
# Печатаем значение по ключу 'Country' из словаря data2
print(data2['Country'])
# Печатаем значение по ключу 'avg_temp' из словаря data2
print(data2['avg_temp'])


