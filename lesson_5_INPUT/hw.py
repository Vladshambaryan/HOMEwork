
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

# Распаковка списка в отдельные переменные
name, last_name, city, phone, country = person

# Вывод переменных для проверки
print(f"Name: {name}")
print(f"Last Name: {last_name}")
print(f"City: {city}")
print(f"Phone: {phone}")
print(f"Country: {country}")


# входные данные
result1 = "результат операции: 42"
result2 = "результат операции: 514"
result3 = "результат работы программы: 9"

# Получение числа, прибавление 10
index1 = int(result1[20:22]) + 10  # получение числа, прибавление 10
index2 = int(result2[20:25]) + 10  # получение числа, прибавление 10

num1 = result3.index('9')  # первого вхождения символа 9
# начиная с 30-го индекса до конца строки и добавляет к нему срез строки result3 начиная с индекса символа 9
num = result3[30:] + result3[num1:]
index3 = int(num) + 10

print(index1)
print(index2)
print(index3)



students = ['Ivanov', 'Petrov', 'Sidorov']  # имена студентов

subjects = ['math', 'biology', 'geography']

students_str = ', '.join(students)  # создаем строку из элементов списка students

subjects_str = ', '.join(subjects)  # создаем строку из элементов списка subjects

print('Students' + students_str + 'study these subjects: ' + subjects_str)

result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"

# for result_1
num_res_1 = int(result_1[(result_1.index(":") + 2):])

# for result_2
num_res_2 = int(result_2[(result_2.index(":") + 2):])

# for result_3
num_res_3 = int(result_3[(result_3.index(":") + 2):])

print(num_res_1 + 10, num_res_2 + 10, num_res_3 + 10, sep='\n')










