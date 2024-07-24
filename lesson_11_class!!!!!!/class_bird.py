class Bird: # клас тип птица
    wings = True # характеристики птиц крылья
    beak = True # характеристики птиц клюв
    plumage = True # характеристики птиц оперения

    def лететь(self): # умеет лететь
        print('машу крыльями, лечу')
    def ходить(self):# умеет ходить
        pass # для каждой птицы разное


class Воробей(Bird): #воробей
    size = 'small' # маленький
    def ходить(self):# ходит
        print('Прыг, прыг')

class Утка(Bird):# утка птица
    size = 'big' # большой

    def ходить(self): #ходит шагами
        print('шагаю')


chizhik = Воробей() # создаем обьект воробей
pyzhik = Воробей()
pyzhik.size = 'medium'
utka = Утка


print(chizhik.size)
print(pyzhik.size)
print(utka.size)

pyzhik.ходить() #ходить
print(chizhik.wings) # крылья
chizhik.лететь() # летит
