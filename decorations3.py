import requests
import bs4
import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(
                    f'{datetime.datetime.now()} | '
                    f'{old_function.__name__} | '
                    f'args={args} | '
                    f'kwargs={kwargs} | '
                    f'result={result}\n'
                )

            return result

        return new_function

    return __logger


KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'голосов']


@logger('habr.log')
def get_articles():
    url = 'https://habr.com/ru/articles/'
    response = requests.get(url)

    soup = bs4.BeautifulSoup(response.text, features='lxml')
    articles = soup.find_all('article')

    result = []

    for article in articles:
        text = article.get_text(' ', strip=True).lower()

        for keyword in KEYWORDS:
            if keyword.lower() in text:
                title_element = article.find('h2')

                if title_element is None:
                    continue

                title = title_element.get_text(strip=True)

                link_element = title_element.find('a')
                link = 'https://habr.com' + link_element['href']

                date_element = article.find('time')
                date = date_element['datetime']

                result.append((date, title, link))
                break

    return result


articles = get_articles()

for date, title, link in articles:
    print(f'{date} – {title} – {link}')