import os
import requests
import pytest


TOKEN = os.getenv('YANDEX_TOKEN')
BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources'

HEADERS = {
    'Authorization': f'OAuth {TOKEN}'
}


def create_folder(folder_name):
    response = requests.put(
        BASE_URL,
        headers=HEADERS,
        params={'path': folder_name}
    )
    return response


def get_folder(folder_name):
    response = requests.get(
        BASE_URL,
        headers=HEADERS,
        params={'path': folder_name}
    )
    return response


def delete_folder(folder_name):
    requests.delete(
        BASE_URL,
        headers=HEADERS,
        params={
            'path': folder_name,
            'permanently': 'true'
        }
    )


def test_create_folder():
    folder_name = 'test_folder_pytest'

    # На случай, если папка осталась от предыдущего запуска
    delete_folder(folder_name)

    response = create_folder(folder_name)

    # При создании ресурса Яндекс.Диск обычно возвращает 201
    assert response.status_code == 201

    response = get_folder(folder_name)

    assert response.status_code == 200
    assert response.json()['name'] == folder_name

    delete_folder(folder_name)


@pytest.mark.parametrize(
    'folder_name, expected_status',
    [
        ('test_folder_pytest', 409),
        ('', 400),
    ]
)
def test_create_folder_errors(folder_name, expected_status):

    if folder_name == 'test_folder_pytest':
        delete_folder(folder_name)
        create_folder(folder_name)

    response = create_folder(folder_name)

    assert response.status_code == expected_status

    if folder_name:
        delete_folder(folder_name)