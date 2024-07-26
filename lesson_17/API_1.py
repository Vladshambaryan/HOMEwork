import requests


def new_gadget_id():
    body = {
        "name": "Apple iPad Air",
        "data": {
            "Generation": "4th",
            "Price": "519.99",
            "Capacity": "256 GB"
        }
    }
    headers = {"Content_Type": "application/json"}
    response = requests.post(
        "https://api.restful-api.dev/objects",
        json=body,
        headers=headers
    )
    return response.json()["id"]


def delete_new_gadget(gadget_id):
    requests.delete(f"https://api.restful-api.dev/objects/{gadget_id}")


def create_one_gadget():
    body = {
        "name": "Apple iPad Air",
        "data": {
            "Generation": "4th",
            "Price": "519.99",
            "Capacity": "256 GB"
        }
    }
    headers = {"Content_Type": "application/json"}
    response = requests.post(
        "https://api.restful-api.dev/objects",
        json=body,
        headers=headers
    )
    try:
        assert response.status_code == 200
        print('Create test Passed')
    except NameError:
        print('Create test Failed')
    print(response.json()["id"])


def update_one_gadget():
    gadget_id = new_gadget_id()
    body = {
        "name": "Apple iPad Air",
        "data": {
            "Generation": "4th",
            "Price": "519.99",
            "Capacity": "255 GB",
            "color": "silver"
        }
    }
    headers = {"Content_Type": "application/json"}
    response = requests.put(
        f"https://api.restful-api.dev/objects/{gadget_id}",
        json=body,
        headers=headers
    ).json()
    try:
        assert response["data"]["color"] == "silver"
        print('Update test Passed')
    except NameError:
        print('Update test Failed')
    print(response)
    delete_new_gadget(gadget_id)

def update_gadget_name():
    gadget_id = new_gadget_id()
    body = {
        "name": "Apple IPhone"
    }
    headers = {"Content_Type": "application/json"}
    response = requests.patch(
        f"https://api.restful-api.dev/objects/{gadget_id}",
        json=body,
        headers=headers
    ).json()
    try:
        assert response["name"] == "Apple IPhone"
        print('Update test Passed')
    except NameError:
        print('Update test Failed')
    print(response["name"])
    delete_new_gadget(gadget_id)


def delete_gadget():
    gadget_id = new_gadget_id()
    response = requests.delete(f"https://api.restful-api.dev/objects/{gadget_id}")
    try:
        assert response.status_code == 200
        print('Delete test Passed')
    except NameError:
        print('Delete test Failed')
    print(response.status_code)


def get_all_gadgets():
    response = requests.get("https://api.restful-api.dev/objects").json()
    try:
        assert len(response) == 13
        print('Get all test Passed')
    except NameError:
        print('Get all test Failed')


def get_one_gadget():
    gadget_id = new_gadget_id()
    response = requests.get(f"https://api.restful-api.dev/objects/{gadget_id}").json()
    try:
        assert response["id"] == gadget_id
        print('Get one test Passed')
    except NameError:
        print('Get one test Failed')


create_one_gadget()
update_one_gadget()
update_gadget_name()
delete_gadget()
get_all_gadgets()
get_one_gadget()