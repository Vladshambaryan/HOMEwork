from datetime import datetime


date_str = "Jan 15, 2023 - 12:05:33"

date_obj = datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")

full_name = date_obj.strftime("%B")
print(f"Полное название месяца: {full_name}")

formatted = date_obj.strftime("%d.%m.%Y, %H:%M")
print(f"Форматированная дата: {formatted}")



temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
                34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
                29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot = list(filter(lambda temp: temp > 28, temperatures))

max_temp = max(hot)
min_temp = min(hot)
avg_temp = sum(hot) / len(hot)

print(f"Самая высокая температура: {max_temp}")
print(f"Самая низкая температура: {min_temp}")
print(f"Средняя температура: {avg_temp:.2f}")





from datetime import datetime

# Дата в строковом формате
date_str = "Jan 15, 2023 - 12:05:33"

# Преобразование строки в объект datetime
date_obj = datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")

# Получение полного названия месяца
full_name = date_obj.strftime("%B")
print(f"Полное название месяца: {full_name}")

# Форматирование даты в нужный формат
formatted = date_obj.strftime("%d.%m.%Y, %H:%M")
print(f"Форматированная дата: {formatted}")

# Список температур
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
                34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
                29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

# Создание нового списка с жаркими днями (температура выше 28)
hot = list(filter(lambda temp: temp > 28, temperatures))

# Нахождение максимальной, минимальной и средней температуры из нового списка
max_temp = max(hot)
min_temp = min(hot)
avg_temp = sum(hot) / len(hot)

print(f"Самая высокая температура: {max_temp}")
print(f"Самая низкая температура: {min_temp}")
print(f"Средняя температура: {avg_temp:.2f}")
