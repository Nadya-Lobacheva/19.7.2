
from api import PetFriends
from settings import *

pf = PetFriends()

import pytest
import requests



def test_delete_pet_without_id(self):
    # Попытка удалить питомца без указания ID
    status, _ = self.api_client.delete_pet()
    assert status == 400


def test_add_pet_without_authentication():
    # Подготовка данных для отправки запроса
    payload = {'name': 'Fluffy', 'type': 'cat'}
    # Отправка POST-запроса на добавление питомца без авторизации
    response = requests.post('https://example.com/api/pets', json=payload)
    # Проверка ожидаемого кода ошибки
    assert response.status_code == 401
    

def test_add_pet_with_incorrect_animal_type():
    # Подготовка данных для отправки запроса
    payload = {'name': 'Fluffy', 'type': 'bird'}
    # Отправка POST-запроса на добавление питомца с некорректным типом животного
    response = requests.post('https://example.com/api/pets', json=payload, headers={'Authorization': 'Bearer <token>'})
    # Проверка ожидаемого кода ошибки
    assert response.status_code == 400
   
    
def test_add_pet_with_empty_name():
    # Подготовка данных для отправки запроса
    payload = {'name': '', 'type': 'dog'}
    # Отправка POST-запроса на добавление питомца с пустым именем
    response = requests.post('https://example.com/api/pets', json=payload, headers={'Authorization': 'Bearer <token>'})
    # Проверка ожидаемого кода ошибки
    assert response.status_code == 400
    

def test_delete_pet_with_invalid_token():
    # Подготовка данных для отправки запроса
    pet_id = 12345
    headers = {'Authorization': 'Bearer <old_token>'}
    # Отправка DELETE-запроса на удаление питомца со старым ключом авторизации
    response = requests.delete(f'https://example.com/api/pets/{pet_id}', headers=headers)
    # Проверка ожидаемого кода ошибки
    assert response.status_code == 401
    
    
    
def test_invalid_age_cannot_add_pet(name='Орурец', animal_type='кошка', age='XXXXX'):
    """
    Проверяем, что нельзя добавить питомца с некорректным значением возраста.
    """
    # Авторизуемся и добавляем питомца
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Проверяем результат
    if isinstance(age, int):  # проверяем, является ли age числом
        assert result is not None
    else:
        assert status == 400  # ожидаемый статус ответа при некорректных данных
        print('Проверка не пройдена: введены некорректные данные')
    
    
def test_add_new_pet_simple_without_auth():
    """Проверяем, что нельзя добавить нового питомца без авторизации"""
    # Добавляем питомца без авторизации и сверяем результат
    status, result = pf.add_new_pet_simple_without_auth('Огурец', 'кошка', 2)
    assert status == 401
    assert 'Auth failed' in result
    
    
 def test_add_pet_with_special_chars_in_animal_type(name='Кот', age='2', pet_photo='images/Cat.jpg'):
    """Проверяем, что нельзя добавить питомца с использованием специальных символов в поле порода."""
    animal_type = 'Cat%@'
    symbols = '\|?/><=+_~@\'\'#\$%\^&\*\{\}'.
    symbol = []
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(api_key, name, animal_type, age, pet_photo)
    assert status == 200
    for i in symbols:
        if i in result['animal_type']:
            symbol.append(i)
    assert symbol[0] not in result['animal_type'], 'Питомец добавлен с недопустимыми специальными символами в поле порода'
   
  def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if not my_pets['pets']:
        pf.add_new_pet(auth_key, "огурец", "кот", "-1", "images/Cat.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    _, status = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем, что статус ответа равен 200, и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in [pet['id'] for pet in my_pets['pets']]
def test_get_all_pets_with_no_valid_key(filter=''):
    """Проверяем, что нельзя получить список питомцев с неверным ключом"""
    auth_key = {"key": "ea738148a1f19838e1c5d1413877f3691a3731380e733e87"}
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 403, f"Ошибка! Статус ответа сервера {status}. Должен быть 403. Неверный ключ аутентификации." 
      
