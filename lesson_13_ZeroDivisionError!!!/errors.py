def calc(x, y):
    try:
        return int(x) / int(y)
    except ZeroDivisionError:
        print('на ноль делить нельзя')
    except ValueError:
        print('Нужно было ввести числа')
    except (ZeroDivisionError, ValueError):
        print('Ошибка ввода данных')


print(calc(input('number:'), input('number:')))
print('hello!')