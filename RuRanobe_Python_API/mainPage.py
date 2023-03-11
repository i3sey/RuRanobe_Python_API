import requests
from bs4 import BeautifulSoup as bs


def GetListOnMainPage(page=1):
    if page < 1:
        return -1
    URL = f"https://ruranobe.ru/projects{f';page={page}' if page > 1 else ''}"
    r = requests.get(URL)
    soup = bs(r.text, "html.parser")
    name_link = {}
    for name, link in zip(soup.find_all('span', class_='project-card__title'),
                          soup.find_all('a', class_='project-card__link ng-star-inserted')):
        name_link.update({name['title']: f"https://ruranobe.ru{link['href']}"})
    return name_link


if __name__ == '__main__':
    print(GetListOnMainPage())
