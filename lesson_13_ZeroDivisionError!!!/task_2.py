# data_file = open('data.txt', 'r') #  чтение
# data_file = open('data.txt', 'w') #  записать
#
# data_file = open('data.txt', 'a') #  дополнение файла
# data_file.read()
# data_file.close()

# Функция для чтения строк из файла data.txt
def read_file():
    with open('data.txt', 'r') as data_file:
        # Печатает объект файла
        # print(data_file)
        # Читает строки из файла и возвращает по одной строке за раз
        for line in data_file.readlines():
            yield line

# Обрабатывает каждую строку из файла data.txt и записывает в data2.txt
for data_line in read_file():
    with open('data2.txt', 'a') as new_file:
        # Убирает точки и запятые из строки
        data_line = data_line.replace('.', '').replace(',', '')
        # Записывает обратно строку в новый файл data2.txt
        new_file.write(data_line)
