import requests  # Импортируем библиотеку для выполнения HTTP-запросов

def add_object():  # Функция для создания нового объекта
    body = {  # Тело запроса с данными объекта
        "name": "Apple MacBook Pro 16",  # Имя объекта
        "data": {  # Словарь с данными объекта
            "year": 2019,  # Год выпуска
            "price": 1849.99,  # Цена
            "CPU model": "Intel Core i9",  # Модель процессора
            "Hard disk size": "1 TB"  # Объем жесткого диска
        }
    }
    headers = {"Content_Type": "application/json"}  # Заголовки запроса
    response = requests.post(  # Выполняем POST-запрос
        "https://api.restful-api.dev/objects",  # URL для создания объекта
        json=body,  # Передаем тело запроса в формате JSON
        headers=headers  # Передаем заголовки запроса
    )
    try:
        assert response.status_code == 200  # Проверяем, что код ответа 200
        print('Add test Passed')
    except NameError:
        print('Add test Failed')
    assert response.status_code == 200  # Проверяем, что код ответа 200

def object_id():  # Функция для получения ID нового объекта
    body = {  # Тело запроса с данными объекта
        "name": "Apple MacBook Pro 16",  # Имя объекта
        "data": {  # Словарь с данными объекта
            "year": 2019,  # Год выпуска
            "price": 1849.99,  # Цена
            "CPU model": "Intel Core i9",  # Модель процессора
            "Hard disk size": "1 TB"  # Объем жесткого диска
        }
    }
    headers = {"Content_Type": "application/json"}  # Заголовки запроса
    response = requests.post(  # Выполняем POST-запрос
        "https://api.restful-api.dev/objects",  # URL для создания объекта
        json=body,  # Передаем тело запроса в формате JSON
        headers=headers  # Передаем заголовки запроса
    )
    return response.json()["id"]  # Возвращаем ID созданного объекта

def delete_object_id(gadget_id):  # Функция для удаления объекта по его ID
    requests.delete(f"https://api.restful-api.dev/objects/{gadget_id}")  # Выполняем DELETE-запрос для удаления объекта

def update_object():  # Функция для обновления данных объекта
    gadget_id = object_id()  # Получаем ID нового объекта
    body = {  # Тело запроса с обновленными данными объекта
        "name": "Apple MacBook Pro 16",  # Имя объекта
        "data": {  # Словарь с данными объекта
            "year": 2019,  # Год выпуска
            "price": 2049.99,  # Обновленная цена
            "CPU model": "Intel Core i9",  # Модель процессора
            "Hard disk size": "1 TB",  # Объем жесткого диска
            "color": "silver"  # Добавленный цвет
        }
    }
    headers = {"Content_Type": "application/json"}  # Заголовки запроса
    response = requests.put(  # Выполняем PUT-запрос для обновления объекта
        f"https://api.restful-api.dev/objects/{gadget_id}",  # URL с ID объекта для обновления
        json=body,  # Передаем тело запроса в формате JSON
        headers=headers  # Передаем заголовки запроса
    ).json()
    try:
        assert response["data"]["color"] == "silver" # Проверяем, что цвет обновлен правильно
        print('Update test Passed')
    except NameError:
        print('Update test Failed')
    print(response)  # Выводим обновленные данные объекта
    delete_object_id(gadget_id)  # Удаляем объект после тестирования

def update_object_name():  # Функция для обновления имени объекта
    gadget_id = object_id()  # Получаем ID нового объекта
    body = {  # Тело запроса с обновленным именем объекта
        "name": "Apple MacBook Pro 16 (Updated Name)"  # Обновленное имя
    }
    headers = {"Content_Type": "application/json"}  # Заголовки запроса
    response = requests.patch(  # Выполняем PATCH-запрос для частичного обновления объекта
        f"https://api.restful-api.dev/objects/{gadget_id}",  # URL с ID объекта для обновления
        json=body,  # Передаем тело запроса в формате JSON
        headers=headers  # Передаем заголовки запроса
    ).json()
    try:
        assert response["name"] == "Apple MacBook Pro 16 (Updated Name)"  # Проверяем, что имя обновлено правильно
        print('Update test Passed')
    except NameError:
        print('Update test Failed')
    print(response["name"])  # Выводим обновленное имя объекта
    delete_object_id(gadget_id)  # Удаляем объект после тестирования

def delete_object():  # Функция для удаления объекта
    gadget_id = object_id()  # Получаем ID нового объекта
    response = requests.delete(f"https://api.restful-api.dev/objects/{gadget_id}")  # Выполняем DELETE-запрос для удаления объекта
    try:
        assert response.status_code == 200  # Проверяем, что код ответа 200
        print('Delete test Passed')
    except NameError:
        print('Delete test Failed')
    print(response.status_code)  # Выводим код ответа

add_object()  # Создаем новый объект
update_object()  # Обновляем данные объекта
update_object_name()  # Обновляем имя объекта
delete_object()  # Удаляем объект
