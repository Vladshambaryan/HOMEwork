class Car:  # создание классов значений
     def __init__(self, wheels, model, speed):  # метод для установки
         self.speed = speed
         self.model = model
         self.wheels = wheels

     def getAll(avto):  # метод вывода значений
         print("Автомобиль", avto.model, "может ехать со скоростью",
               avto.speed, "на всех", avto.wheels, "колесах!")

ford = Car(4, "ford", 125)
ford.getAll()

audi = Car(4, "Audi", 250)
audi.getAll()

bmw = Car(4, "bmw", 225)
bmw.getAll()

lexus = Car(4, "Lexus", 250)
lexus.getAll()

chevrolet = Car(4, "chevrolet", 160)
chevrolet.getAll()

