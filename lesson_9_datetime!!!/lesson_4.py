import datetime  # Импортируем модуль datetime для работы с датой и временем

# Получаем текущую дату и время
time_now = datetime.datetime.now()
print(time_now)  # Выводим текущее дату и время
print(time_now.hour)  # Выводим текущий час
print(time_now.year)  # Выводим текущий год
print(time_now.isoweekday())  # Выводим номер дня недели (1 - понедельник, 7 - воскресенье)
print(time_now.timestamp())  # Выводим количество секунд с начала эпохи Unix (1 января 1970 года)

# Создаем объект datetime с заданной датой
easy_date = datetime.datetime(2000, 1, 15)
print(easy_date)  # Выводим заданную дату
print(easy_date.timestamp())  # Выводим количество секунд с начала эпохи Unix для заданной даты

# Парсим строку даты и времени в объект datetime
my_time = '2023/06/05 12 hours, 30 mins, 10 secs'
python_date = datetime.datetime.strptime(my_time, '%Y/%m/%d %H hours, %M mins, %S secs')

print(python_date)  # Выводим объект datetime, созданный из строки
print(python_date.month)  # Выводим месяц из объекта datetime

# Преобразуем объект datetime в строку определенного формата
human_date = python_date.strftime('Year: %y, month: %B, day: %d')
print(human_date)  # Выводим строку с датой в заданном формате

