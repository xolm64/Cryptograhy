import requests
from requests import Response

Response

response = requests.get("https://ergo-store.ru/wp-content/uploads/2021/01/Luchshee-ortopedicheskoe-kreslo-dlya-raboty-za-kompyuterom.jpg")

print(response.status_code) # если 200 то все правильно , 404 не правильно

print(type(response))

with open('im1.jpeg' , 'wb') as f:
    f.write(response.content)

