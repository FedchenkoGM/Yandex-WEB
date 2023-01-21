import requests


geocoder_request = "https://geocode-maps.yandex.ru/1.x/\
?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Москва, Петровка, 38&format=json"

# Выполняем запрос.
response = requests.get(geocoder_request)
if response:
    # Преобразуем ответ в json-объект
    json_response = response.json()
    # print(json_response)

    # Получаем первый топоним из ответа геокодера.
    # Согласно описанию ответа, он находится по следующему пути:
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    # Полный адрес топонима:
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    # Координаты центра топонима:
    toponym_postal_code = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
    # Печатаем извлечённые из ответа поля:
    print(toponym_address, "имеет почтовый индекс:", toponym_postal_code)
else:
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")