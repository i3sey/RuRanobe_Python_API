from bs4 import BeautifulSoup as bs
import requests


def downloadLinks(link):
    r = requests.get(link)
    soup = bs(r.text, "html.parser")
    links = {}
    new_var = soup.find_all('div', class_='download__buttons')
    for form in new_var:
        for an in form:
            links.update({an.text: f"https://ruranobe.ru{an['href']}"})
    return links


print(downloadLinks('https://ruranobe.ru/r/tnynn/v1'))
