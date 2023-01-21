import requests
import os
import sys
import pygame


points = ['Спартак', 'Динамо', 'Лужники']
coords = []

for point in points:
    geocoder_request = f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Москва, {point}&format=json"

    # Выполняем запрос.
    response = requests.get(geocoder_request)
    json_response = response.json()

    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    print(json_response)
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    # Печатаем извлечённые из ответа поля:
    print(toponym_coodrinates)
    coords.append(toponym_coodrinates)

coord = [x.replace(' ', ',') for x in coords]
print('~'.join(coord))
map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord[2]}&spn=0.2,0.2&l=map&size=650,450&pt={'~'.join(coord)}"
response = requests.get(map_request)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((650, 450))
pygame.display.set_caption('Москва. Стадионы')
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
