import requests
from bs4 import BeautifulSoup as bs


def get_status(link):
    r = requests.get(link)
    soup = bs(r.text, "html.parser")
    return soup.find_all('span', class_='text--ellipsis')[0].text


if __name__ == '__main__':
    print(get_status('https://ruranobe.ru/r/tnynn'))
