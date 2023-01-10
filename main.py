import requests
from bs4 import BeautifulSoup


headers = {
    'Host': 'hh.ru',
    'User-Agent': 'Safari',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
#Создание запроса GET к странице с вакансиями
hh_request = requests.get('https://hh.ru/search/vacancy?area=1&text=python&items_on_page=100', headers=headers)
print(hh_request.text)
print("--------")
#Извлекаем html разметку страницы
hh_soup = BeautifulSoup(hh_request.text, 'html.parser')
#Нашли пагинатор по отдельному классу в разметке, используя метод библиотеки BeatifulSoup
paginator = hh_soup.find("div", {'class': 'pager'})
#Извлекаем ссылки из пагинатора
pages = paginator.findAll('a')

print(pages)