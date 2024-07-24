import json

class CountryData:
    def __init__(self, filename):
        self.__filename = filename
        self.__data = self.__read_file()
        self.__country = self.__data['Country']
        self.__avg_temp = self.__data['avg_temp']
        self._comfort = self.__is_comfort()

    @property
    def data(self):
        return self.__data

    @property
    def country(self):
        return self.__country

    @property
    def avg_temp(self):
        return self.__avg_temp

    @property
    def comfort(self):
        return self._comfort

    @comfort.setter
    def comfort(self, value):
        self._comfort = value

    def __read_file(self):
        with open(self.__filename, 'r') as file_data:
            data = json.load(file_data)
        return data

    def __is_comfort(self):
        return self.__avg_temp > 25

    def __str__(self):
        return f'str File {self.__filename} with data {self.__data}'

    def __repr__(self):
        return f'repr File {self.__filename} with data {self.__data}'

    def __lt__(self, obj):
        return self.avg_temp < obj.avg_temp

    def __le__(self, obj):
        return self.avg_temp <= obj.avg_temp

    def __add__(self, obj):
        return [self, obj]

# Создание объектов и выполнение операций
data1 = CountryData('data/data1.txt')
data1.comfort = False  # Установка нового значения для comfort
print(data1.comfort)   # False

print(data1.data)      # {'Country': 'Armenia', 'avg_temp': 30}

# Следующие строки закомментированы, потому что они изменяют приватные данные напрямую:
# data1.data = 'skdfjhskdjf'    # Ошибка: нельзя напрямую изменить атрибут через свойство
# data1.__data = {'1': 5}       # Не меняет ничего в объекте из-за наличия __ в имени атрибута

print(data1.data)      # {'Country': 'Armenia', 'avg_temp': 30} - данные остаются неизменными
print(data1.country)   # Armenia

data2 = CountryData('data/data2.txt')
print(data2.country)   # Greece

data1.__avg_temp = 2342342  # Это добавляет новый атрибут __avg_temp, а не изменяет существующий
print(data1.avg_temp)       # 30 - потому что доступ к приватному атрибуту через @property не изменился



class CountryDataWithMinTemp(CountryData):
    def __init__(self, filename):
        super().__init__(filename)
        self.min_temp = self.data['min_temp']


data3 = CountryDataWithMinTemp('data/data3.txt')
print(data3.avg_temp)
print(data3.min_temp)



print(data1)  # print(str(data1))
print(data1 < data2)
print(data1 <= data2)
print(data1 > data2)
print(data1 >= data2)
print(data1 + data2)