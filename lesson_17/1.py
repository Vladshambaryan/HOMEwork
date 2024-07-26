import  requests


def post_test():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    assert response.status_code == 200
    print(response.status_code)


def new_id():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    return response.json()["id"]


def delete_new_id(gadjet_id):
    requests.delete(f"https://api.restful-api.dev/objects/{gadjet_id}")


def update():
    gadjet_id = new_id()
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"

        }
    }
    headers = {"Content_Type": "application/json"}
    response = requests.put(f"https://api.restful-api.dev/objects/{gadjet_id}", json=body, headers=headers).json()
    assert response["data"]["year"] == 2019," цвет не существует"
    assert response["data"]["price"] == 2049.99," цвет не существует"
    assert response["data"]["CPU model"] == "Intel Core i9"," цвет не существует"
    assert response["data"]["color"] == "silver"," цвет не существует"
    assert response["name"] == "Apple MacBook Pro 16"
    print(response)
    delete_new_id(gadjet_id)


def update_object_name():  # Функция для обновления имени объекта
    gadget_id = new_id()  # Получаем ID нового объекта
    body = {  # Тело запроса с обновленным именем объекта
        "name": "Apple MacBook Pro 16 (Updated Name)"  # Обновленное имя
    }
    headers = {"Content_Type": "application/json"}  # Заголовки запроса
    response = requests.patch(  # Выполняем PATCH-запрос для частичного обновления объекта
        f"https://api.restful-api.dev/objects/{gadget_id}",  # URL с ID объекта для обновления
        json=body,  # Передаем тело запроса в формате JSON
        headers=headers  # Передаем заголовки запроса
    ).json()
    assert response["name"] == "Apple MacBook Pro 16 (Updated Name)"  # Проверяем, что имя обновлено правильно
    print(response["name"])  # Выводим обновленное имя объекта
    delete_new_id(gadget_id)  # Удаляем объект после тестирования


post_test()
update()
update_object_name()
