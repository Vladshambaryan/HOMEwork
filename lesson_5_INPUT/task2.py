result1 = "результат операции: 42"
result2 = "результат операции: 9999984"
result3 = "результат работы программы: 9"

index1 = result1.index(':')  # находим индекс ':'
number1 = int(result1[index1 + 2:])  # отрезаем все после ':'

index2 = result2.index(':')  # находим индекс ':'
number2 = int(result2[index2 + 2:])  # отрезаем все после ':'
number2 += 10  # прибавляем 10

index3 = result3.index(':')  # находим индекс ':'
number3 = int(result3[index3 + 2:])  # отрезаем все после ':'
number3 += 10  # прибавляем 10

# Печатаем результаты
print(number1)
print(number2)
print(number3)



result1 = "результат операции: 42"
result2 = "результат операции: 514"
result3 = "результат работы программы: 9"

number1 = int(result1[result1.index(':') + 2:])

number2 = int(result2[result2.index(':') + 2:])

number3 = int(result3[result3.index(':') + 2:])

print(number1 + 10, number2 + 10, number3 + 10)



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