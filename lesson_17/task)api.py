import requests  # Импортируем библиотеку для выполнения HTTP-запросов

def add_object():  # Функция для добавления нового объекта
    body = {  # Тело запроса с данными объекта
        "name": "Apple MacBook Pro 16",  # Название объекта
        "data": {  # Данные объекта
            "year": 2019,  # Год выпуска
            "price": 1849.99,  # Цена
            "CPU model": "Intel Core i9",  # Модель процессора
            "Hard disk size": "1 TB"  # Объем жесткого диска
        }
    }
    headers = {"Content-Type": "application/json"}  # Заголовки запроса
    response = requests.post(  # Выполняем POST-запрос
        "https://api.restful-api.dev/objects",  # URL для создания объекта
        json=body,  # Передаем тело запроса в формате JSON
        headers=headers  # Передаем заголовки запроса
    )
    # Проверяем, что статус-код 200 и есть ID в ответе
    assert response.status_code == 200, f"Не удалось добавить объект: {response.status_code}, {response.text}"
    json_response = response.json()  # Преобразуем ответ в JSON
    assert "id" in json_response, "ID не найдено в ответе"  # Проверяем, что ID присутствует в ответе
    print(f"Объект добавлен с ID: {json_response['id']}")  # Выводим ID нового объекта

def object_id():  # Функция для получения ID нового объекта
    body = {  # Тело запроса с данными объекта
        "name": "Apple MacBook Pro 16",  # Название объекта
        "data": {  # Данные объекта
            "year": 2019,  # Год выпуска
            "price": 1849.99,  # Цена
            "CPU model": "Intel Core i9",  # Модель процессора
            "Hard disk size": "1 TB"  # Объем жесткого диска
        }
    }
    headers = {"Content-Type": "application/json"}  # Заголовки запроса
    response = requests.post(  # Выполняем POST-запрос
        "https://api.restful-api.dev/objects",  # URL для создания объекта
        json=body,  # Передаем тело запроса в формате JSON
        headers=headers  # Передаем заголовки запроса
    )
    assert response.status_code == 200, f"Не удалось создать объект: {response.status_code}, {response.text}"  # Проверяем статус-код
    json_response = response.json()  # Преобразуем ответ в JSON
    assert "id" in json_response, "ID не найден в ответе"  # Проверяем, что ID присутствует в ответе
    return json_response["id"]  # Возвращаем ID нового объекта

def delete_object_id(gadget_id):  # Функция для удаления объекта по его ID
    response = requests.delete(f"https://api.restful-api.dev/objects/{gadget_id}")  # Выполняем DELETE-запрос для удаления объекта
    assert response.status_code == 200, f"Не удалось удалить объект: {response.status_code}, {response.text}"  # Проверяем статус-код

def update_object():  # Функция для обновления данных объекта
    gadget_id = object_id()  # Получаем ID нового объекта
    body = {  # Тело запроса с обновленными данными объекта
        "name": "Apple MacBook Pro 16",  # Название объекта
        "data": {  # Данные объекта
            "year": 2019,  # Год выпуска
            "price": 2049.99,  # Обновленная цена
            "CPU model": "Intel Core i9",  # Модель процессора
            "Hard disk size": "1 TB",  # Объем жесткого диска
            "color": "silver"  # Цвет объекта
        }
    }
    headers = {"Content-Type": "application/json"}  # Заголовки запроса
    response = requests.put(  # Выполняем PUT-запрос для обновления объекта
        f"https://api.restful-api.dev/objects/{gadget_id}",  # URL с ID объекта для обновления
        json=body,  # Передаем тело запроса в формате JSON
        headers=headers  # Передаем заголовки запроса
    )
    assert response.status_code == 200, f"Не удалось обновить объект: {response.status_code}, {response.text}"  # Проверяем статус-код
    json_response = response.json()  # Преобразуем ответ в JSON
    assert json_response["data"]["color"] == "silver", "Цвет не правильно обновлен"  # Проверяем, что цвет обновлен правильно
    print(json_response)  # Выводим обновленные данные объекта
    delete_object_id(gadget_id)  # Удаляем объект после тестирования

def update_object_name():  # Функция для обновления имени объекта
    gadget_id = object_id()  # Получаем ID нового объекта
    body = {  # Тело запроса с обновленным именем объекта
        "name": "Apple MacBook Pro 16 (Updated Name)"  # Обновленное имя
    }
    headers = {"Content-Type": "application/json"}  # Заголовки запроса
    response = requests.patch(  # Выполняем PATCH-запрос для частичного обновления объекта
        f"https://api.restful-api.dev/objects/{gadget_id}",  # URL с ID объекта для обновления
        json=body,  # Передаем тело запроса в формате JSON
        headers=headers  # Передаем заголовки запроса
    )
    assert response.status_code == 200, f"Не удалось обновить имя объекта: {response.status_code}, {response.text}"  # Проверяем статус-код
    json_response = response.json()  # Преобразуем ответ в JSON
    assert json_response["name"] == "Apple MacBook Pro 16 (Updated Name)", "Имя обновлено неправильно"  # Проверяем, что имя обновлено правильно
    print(json_response["name"])  # Выводим обновленное имя объекта
    delete_object_id(gadget_id)  # Удаляем объект после тестирования

def delete_object():  # Функция для удаления объекта
    gadget_id = object_id()  # Получаем ID нового объекта
    response = requests.delete(f"https://api.restful-api.dev/objects/{gadget_id}")  # Выполняем DELETE-запрос для удаления объекта
    assert response.status_code == 200, f"Не удалось удалить объект: {response.status_code}, {response.text}"  # Проверяем статус-код
    print(response.status_code)  # Выводим статус-код ответа

add_object()  # Создаем новый объект
update_object()  # Обновляем данные объекта
update_object_name()  # Обновляем имя объекта
delete_object()  # Удаляем объект
