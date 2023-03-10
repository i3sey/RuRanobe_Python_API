import requests
from bs4 import BeautifulSoup as bs

def get_tags(link):
    r = requests.get(link)
    soup = bs(r.text, "html.parser")
    return [tag.text for tag in soup.find_all('a', class_ = 'genres__item')][1:]

if __name__ == '__main__':
    print(get_tags('https://ruranobe.ru/r/tnynn'))