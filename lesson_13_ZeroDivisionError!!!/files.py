import os

# Печатает текущую директорию файла
# print(os.path.dirname(__file__))

# Определяет базовый путь текущего файла
base_path = os.path.dirname(__file__)
# Определяет путь к файлу data.txt в текущей директории
# file_path = f'{base_path}\data.txt'
file_path = os.path.join(base_path, 'data.txt')
# Определяет путь к новому файлу data2.txt в текущей директории
new_file_path = os.path.join(base_path, 'data2.txt')
print(file_path)

# Функция для чтения строк из файла data.txt
def read_file():
    with open(file_path, 'r') as data_file:
        # Читает строки из файла и возвращает по одной строке за раз
        for line in data_file.readlines():
            yield line

# Обрабатывает каждую строку из файла data.txt и записывает в data2.txt
for data_line in read_file():
    with open(new_file_path, 'a') as new_file:
        # Убирает точки и запятые из строки
        data_line = data_line.replace('.', '').replace(',', '')
        # Записывает обработанную строку в новый файл data2.txt
        new_file.write(data_line)

# Определяет путь к домашней директории одного уровня выше текущей директории
homework_path = os.path.dirname(os.path.dirname(base_path))
# Определяет путь к файлу vlad.txt в поддиректории Okulik.by
vlad_file_path = os.path.join(homework_path, 'homework', 'vlad.txt')
print(vlad_file_path)

# Открывает и читает файл vlad.txt, печатает его содержимое
with open(vlad_file_path) as vlad_file:
    print(vlad_file.read())
