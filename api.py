import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'

#Получение информации об одном животном:

def get_animal_types(self) -> json:
    """Метод отправляет запрос на сервер для получения списка доступных для выбора видов животных и возвращает
    статус запроса и result в формате JSON со списком видов животных"""

    res = requests.get(self.base_url + 'api/animal_types')

    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(result)
    return status, result
  
  
  
  #Получение списка животных, принадлежащих определенному пользователю:
  
  def get_user_pets(self, user_id: str) -> json:
    """Метод отправляет запрос на сервер для получения списка животных, принадлежащих определенному пользователю,
    и возвращает статус запроса и result в формате JSON со списком животных"""

    res = requests.get(self.base_url + 'api/users/' + user_id + '/pets')

    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(result)
    return status, result
  
  
  #Обновление фотографии животного:
  
  def update_pet_photo(self, auth_key: json, pet_id: str, photo_path: str) -> json:
    """Метод отправляет запрос на сервер для обновления фотографии животного по указанному ID и возвращает
    статус запроса и result в формате JSON с обновленными данными животного"""

    headers = {'auth_key': auth_key['key']}
    files = {'file': open(photo_path, 'rb')}

    res = requests.put(self.base_url + 'api/pets/' + pet_id + '/photo', headers=headers, files=files)

    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(result)
    return status, result
  
  
  
  # Отправка запроса на сервер с целью обновления информации о питомце по указанному ID и получения этой информации в формате JSON
  def update_pet_info(self, auth_key: json, pet_id: str, name: str,
                        animal_type: str, age: int) -> json:
        """Метод отправляет запрос на сервер о обновлении данных питомца по указанному ID и
        возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""
        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'age': age,
            'animal_type': animal_type
        }
        res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

  
  
  #Получение списка доступных для выбора видов животных:
  
  def get_animal_types(self) -> json:
    """Метод отправляет запрос на сервер для получения списка доступных для выбора видов животных и возвращает
    статус запроса и result в формате JSON со списком видов животных"""

    res = requests.get(self.base_url + 'api/animal_types')

    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(result)
    return status, result

  
  
  
  
  
  

 
