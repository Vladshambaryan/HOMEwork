# все типы обьектов являются описанием обьектов
from abc import abstractmethod

# Базовый класс Group определяет общие атрибуты и методы для всех групп учеников
class Group:
    pupils = True  # Общий атрибут класса, указывающий, что группы имеют учеников
    school_name = 42  # Общий атрибут класса, представляющий имя школы (в данном случае это число)
    director = 'Marivanna'  # Общий атрибут класса, представляющий имя директора школы

    def __init__(self, title, pupils_count, group_leader):
        # Конструктор класса, инициализирующий объект с заголовком группы, количеством учеников и лидером группы
        self.title = title
        self.pupils_count = pupils_count
        self.group_leader = group_leader

    def study(self):
        # Метод для вывода сообщения о процессе обучения
        print('sit down and read')

    @abstractmethod
    def move(self):
        # Абстрактный метод, который должен быть реализован в дочерних классах
        pass

# Дочерний класс PrimaryGroup определяет атрибуты и методы для начальной группы учеников
class PrimaryGroup(Group):
    max_age = 11  # Максимальный возраст учеников в начальной группе
    min_age = 6  # Минимальный возраст учеников в начальной группе
    building_section = 'left'  # Секция здания, в которой находится начальная группа

    def __init__(self, title, pupils_count, group_leader, class_room):
        # Конструктор класса, инициализирующий объект с дополнительным атрибутом class_room
        super().__init__(title, pupils_count, group_leader)
        self.class_room = class_room

    def move(self):
        # Реализация абстрактного метода move для начальной группы учеников
        print('Run fast')

# Дочерний класс HighGroup определяет атрибуты и методы для старшей группы учеников
class HighGroup(Group):
    max_age = 18  # Максимальный возраст учеников в старшей группе
    min_age = 14  # Минимальный возраст учеников в старшей группе

    def move(self):
        # Реализация абстрактного метода move для старшей группы учеников
        print('Go slowly')

# Дочерний класс MediumGroup определяет атрибуты для средней группы учеников
class MediumGroup(Group):
    max_age = 15  # Максимальный возраст учеников в средней группеl
    min_age = 10  # Минимальный возраст учеников в средней группе

    def move(self):
        # Реализация абстрактного метода move для средней группы учеников
        print('Walk at a moderate pace')

# Создание объектов начальной группы
first_a = PrimaryGroup('1a', 18, 'MF', 5)
first_b = PrimaryGroup('1b', 20, 'TD', 8)

# Создание объектов старшей и средней группы
eleven_a = HighGroup('11a', 22, 'AR')
six_a = MediumGroup('6a', 25, 'RI')

# Вывод атрибутов и выполнение методов для объектов начальной, старшей и средней группы
print(first_a.pupils_count)  # Вывод количества учеников в первой начальной группе
print(first_a.class_room)  # Вывод номера класса первой начальной группы
print(first_b.title)  # Вывод названия второй начальной группы
print(first_a.title)  # Вывод названия первой начальной группы
print(first_a.pupils)  # Вывод атрибута pupils для первой начальной группы
print(first_a.building_section)  # Вывод секции здания для первой начальной группы
print(first_a.director)  # Вывод имени директора для первой начальной группы
print(first_a.max_age)  # Вывод максимального возраста учеников в первой начальной группе
print(first_a.min_age)  # Вывод минимального возраста учеников в первой начальной группе
print(first_a.school_name)  # Вывод имени школы для первой начальной группы
print(eleven_a.pupils)  # Вывод атрибута pupils для старшей группы
# print(eleven_a.building_section)  # Закомментировано, так как старшая группа не имеет атрибута building_section
print(eleven_a.director)  # Вывод имени директора для старшей группы
print(eleven_a.max_age)  # Вывод максимального возраста учеников в старшей группе
print(eleven_a.min_age)  # Вывод минимального возраста учеников в старшей группе
print(eleven_a.school_name)  # Вывод имени школы для старшей группы

# Выполнение метода study для объектов первой начальной и старшей группы
first_a.study()
eleven_a.study()

# Выполнение метода move для объектов первой начальной, старшей и средней группы
first_a.move()
eleven_a.move()
six_a.move()
