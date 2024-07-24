class Car:

    def __init__(self, wheels, model, speed, mirror, horn, trunk):
        # Атрибуты экземпляра, специфичные для каждого объекта
        self.speed = speed
        self.model = model
        self.wheels = wheels
        self.mirror = mirror
        self.horn = horn
        self.trunk = trunk

    def getAll(self):
        # Метод экземпляра для вывода информации об автомобиле
        print("авто", self.model, "может ехать со скоростью", self.speed, "на всех", self.wheels, "колесах!")
        print("авто", self.model, "имеет", self.mirror, "mirror(s),", self.horn, "horn(s),", self.trunk, "trunk(s)")

# Создание объектов класса Car и вызов метода getAll для каждого объекта
ford = Car(4, "Ford", 125, 3, 2, 1)
ford.getAll()

audi = Car(4, "Audi", 250, 3, 3, 1)
audi.getAll()

bmw = Car(4, "BMW", 225, 3, 2, 1)
bmw.getAll()

lexus = Car(4, "Lexus", 250, 3, 3, 1)
lexus.getAll()

chevrolet = Car(4, "chevrolet", 160, 3, 3, 1)
chevrolet.getAll()