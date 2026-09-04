import requests
import bs4

url = 'https://habr.com/ru/articles/'
response = requests.get(url)

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

soup = bs4.BeautifulSoup(response.text, features='lxml')

articles = soup.find_all('article')

for article in articles:
    text = article.get_text(' ', strip=True).lower()

    for keyword in KEYWORDS:
        if keyword.lower() in text:
            title_element = article.find('h2')
            title = title_element.get_text(strip=True)

            link_element = title_element.find('a')
            link = 'https://habr.com' + link_element['href']

            date_element = article.find('time')
            date = date_element['datetime']

            print(f'{date} – {title} – {link}')
            break
