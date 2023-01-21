import requests


for town in ['Барнаул', 'Мелеуз', 'Йошкар-Ола', 'Благовещенск']:
    geocoder_request = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={town}&format=json"

    # Выполняем запрос.
    response = requests.get(geocoder_request)
    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()
        # print(json_response)

        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_province = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][2]["name"]
        # Печатаем извлечённые из ответа поля:
        print(town + ':', toponym_province)
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")