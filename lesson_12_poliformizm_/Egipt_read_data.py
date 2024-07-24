import json

# Читаем данные из файла 'data/egypt.json' и загружаем их в формате JSON
with open('data/egypt.json', 'r') as country_file:
    file_data = json.load(country_file)

# Выводим страну, максимальную и минимальную температуру из файла
print(file_data['Country'])
print(file_data['max_temp'])
print(file_data['min_temp'])

class CountryData:
    def __init__(self, file_path):
        self.file_path = file_path  # self из объекта дай файл file_path
        self.file_data = self.read_data()  # self Из объекта берем
        self.country = self.file_data['Country']  # self Из объекта берем страну
        self.max_temp = self.file_data['max_temp']  # self Из объекта берем максимальную температуру
        self.min_temp = self.file_data['min_temp']  # self Из объекта берем минимальную температуру

    # Метод для чтения данных из файла
    def read_data(self):
        with open(self.file_path, 'r') as country_file:
            return json.load(country_file)

    # Метод для проверки комфортности страны по температуре
    def is_comfortable(self):
        return self.max_temp - self.min_temp > 10

class CountryDataWithSunDays(CountryData):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.sunny_days = self.file_data.get('sunny_days', 0)  # Добавляем атрибут солнечных дней

    # Переопределяем метод для проверки комфортности с учетом солнечных дней
    def is_comfortable(self):
        return self.max_temp - self.min_temp + self.sunny_days > 10

# Создаем экземпляры классов для Египта и Швеции
egypt = CountryData('data/egypt.json')
sweden = CountryDataWithSunDays('data/sweden.json')

# Выводим информацию об Египте
print(egypt.file_path)
print(egypt.max_temp)
print(egypt.min_temp)
print(egypt.country)

# Выводим информацию о Швеции
print(sweden.file_path)
print(sweden.max_temp)
print(sweden.min_temp)
print(sweden.country)
print(sweden.sunny_days)


''' Наследование это когда  Дочерние элемент наследуют сохраняют  функциональность от родительского класса,
 расширяя и дополняя её.
'''

'''Инкапсуляция это способность  хранить все данные в себе
Все данные объекта должны хранится в объекте. Никто не может 
изменить данные объекта без его ведома.
правила Инкапсуляции есть подходы по обзыванию __ защищеные, _менее защищеные, не защищеные.
'''

'''Полиморфизм
Способность классов менять своё поведение в зависимости от типов операций и операндов.
Полиморфизм в программировании реализуется через перегрузку метода, 
либо через его переопределение.

'''