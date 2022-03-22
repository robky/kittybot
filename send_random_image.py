from telegram import Bot
import requests

bot = Bot(token='5052093685:AAEL7rHh1-KfwEblWE7gIvTLlJ-9pxDF05M')
URL = 'https://api.thecatapi.com/v1/images/search'
chat_id = 353952708

# Делаем GET-запрос к эндпоинту:
response = requests.get(URL).json()
# Извлекаем из ответа URL картинки:
random_cat_url = response[0].get('url')  

# Передаём chat_id и URL картинки в метод для отправки фото:
bot.send_photo(chat_id, random_cat_url)
