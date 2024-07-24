import random


salary = int(input("Введите вашу зарплату: "))

# Генерируем случайное значение для bonus (True или False)
bonus = random.choice([True, False])

if bonus:
    # Если bonus равен True, то к salary добавляется случайный бонус от 0 до 5000
    bonus_amount = random.randint(0, 5000)
    salary += bonus_amount

# Выводим итоговую зарплату, форматируя её в виде строки с символом '$'
print(f'${salary}')
