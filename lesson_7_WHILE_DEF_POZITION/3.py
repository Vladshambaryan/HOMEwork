# Пример с возвратом значения из функции
a = 1
b = 5
c = 4
d = 7
y = 1

# Основное число для добавления
main_number = 47

# Определение функции calc, которая принимает один аргумент numb и возвращает результат
def calc(numb):
    # Если y равно 0, возвращает numb, иначе возвращает numb + main_number
    if y == 0:
        return numb
    else:
        result = numb + main_number
        return result

# Печатает результат вызова функции calc с аргументом a
print(calc(a))
# Вывод: 48

def hello():
    a = 12
    return None

print(hello())
None









