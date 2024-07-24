# Пример функции с позиционным, произвольным числом аргументов и именованными аргументами
def price_list(list_title, *args, default_qty=234, **kwargs):
    # Печатает заголовок списка
    print(list_title)
    # Проходит по именованным аргументам и печатает каждую пару ключ-значение
    for title, price in kwargs.items():
        print(f'Product {title} price is {price}')

# Вызов функции с позиционным, произвольным числом и именованными аргументами
price_list('Products prices', iphone=2500, laptop=1500, samsung=2000, monitor=1000)
# Вывод: Products prices, Product iphone price is 2500, Product laptop price is 1500, Product samsung price is 2000, Product monitor price is 1000


# Пример функции с двумя аргументами
def price_list(title, price):
    print(f'Product {title} price is {price}')

# Вызов функции с двумя аргументами
price_list('iphone', 2500)
price_list('laptop', 1500)
# Вывод: Product iphone price is 2500, Product laptop price is 1500

# Пример функции с произвольным числом позиционных аргументов
def sum_all(*args):
    # Суммирует все аргументы и возвращает результат
    return sum(args)

# Вызов функции с произвольным числом аргументов
print(sum_all(1, 4, 6, 5, 7))
# Вывод: 23
