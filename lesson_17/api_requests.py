import requests  # Импортируем библиотеку для выполнения HTTP-запросов
import json  # Импортируем библиотеку для работы с JSON-данными

# Функция для получения всех постов
def all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200  # Проверяем, что статус код ответа 200 (OK)
    data = response.json()
    assert len(data) > 0  # Проверяем, что полученные данные не пусты

all_posts()

# Функция для получения одного поста
def one_post():
    post_id = 42
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
    assert response.status_code == 200  # Проверяем, что статус код ответа 200 (OK)
    data = response.json()
    assert data['id'] == post_id  # Проверяем, что ID полученного поста совпадает с запрашиваемым ID
    print(data)
    print(response.status_code)

one_post()

# Функция для создания нового поста
def post_a_post():
    body = {
       "title": "foooooooo",
       "body": "baposttttttttttttt",
       "userId": 1
    }
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    assert response.status_code == 201  # Проверяем, что статус код ответа 201 (Created)
    data = response.json()
    assert data['title'] == body['title']  # Проверяем, что заголовок поста совпадает с отправленным
    print(data)
    print(response.status_code)

post_a_post()

# Функция для обновления существующего поста
def put_a_post():
    body = {
       "title": "foooooooo",
       "body": "baaaaaputttttttttttttr",
       "userId": 1
    }
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.put(
        'https://jsonplaceholder.typicode.com/posts/42',
        json=body,
        headers=headers
    )
    assert response.status_code == 200  # Проверяем, что статус код ответа 200 (OK)
    data = response.json()
    assert data['title'] == body['title']  # Проверяем, что заголовок обновленного поста совпадает с отправленным
    print(data)
    print(response.status_code)

put_a_post()

# Функция для частичного обновления существующего поста
def patch_a_post():
    body = {
       "title": "foooooooo",
       "body": "baaaapatchhhhhh",
       "userId": 7
    }
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.patch(
        'https://jsonplaceholder.typicode.com/posts/42',
        json=body,
        headers=headers
    )
    assert response.status_code == 200  # Проверяем, что статус код ответа 200 (OK)
    data = response.json()
    assert data['body'] == body['body']  # Проверяем, что тело обновленного поста совпадает с отправленным
    print(data)
    print(response.status_code)

patch_a_post()

# Функция для удаления существующего поста
def delete_a_post():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/42')
    assert response.status_code == 200  # Проверяем, что статус код ответа 200 (OK)
    print(response.status_code)

delete_a_post()



































#
#
#
#
#
