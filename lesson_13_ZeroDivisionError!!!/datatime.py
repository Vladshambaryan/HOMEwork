import datetime  # Импортируем модуль datetime

# Получаем текущее время и дату
now = datetime.datetime.now()
print(now)

# Создаем объект datetime, представляющий полночь текущего дня
today_midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
print(today_midnight)

# Вычисляем разницу между текущим временем и полночью
after_midnight = now - today_midnight
# Выводим количество секунд, прошедших с полуночи
print(after_midnight.seconds)

# Выводим объект timedelta, представляющий разницу между текущим временем и полночью
print(after_midnight)

# Вычисляем дату и время через 10 дней и 10 часов от текущего момента и выводим результат
print(now + datetime.timedelta(days=10, hours=10))
