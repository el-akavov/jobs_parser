import requests
from bs4 import BeautifulSoup

headers = {
    'Host': 'hh.ru',
    'User-Agent': 'Safari',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
ITEMS = 100
URL = f'https://hh.ru/search/vacancy?area=1&text=python&items_on_page={ITEMS}'


def extract_max_page():
    # Создание запроса GET к странице с вакансиями
    hh_request = requests.get(URL, headers=headers)
    print(hh_request)
    print("--------")

    # Извлекаем html разметку страницы
    hh_soup = BeautifulSoup(hh_request.text, 'html.parser')

    # Нашли пагинатор по отдельному классу в разметке, используя метод библиотеки BeatifulSoup
    paginator = hh_soup.findAll("span", {'class': 'pager-item-not-in-short-range'})

    # Извлекаем ссылки из пагинатора
    pages = []
    for page in paginator:
        pages.append(int(page.find('a').text))

    return pages[-1]


def extract_hh_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f'{URL}&page={page}', headers)
        print(result.status_code)
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.findAll('div', {'class': 'vacancy-serp-item'})
        for result in results:
            result.find('a').text
    return jobs