import requests
from bs4 import BeautifulSoup as bs
from lxml import etree

def get_volumes(link):
    r = requests.get(link)
    soup = bs(r.text, "html.parser")
    dom = etree.HTML(str(soup))
    vols = {}
    for vol in soup.find_all('a', class_="list__item"):
        vols.update({f'{vol.text}' : f"https://ruranobe.ru{vol['href']}"})
    return vols

if __name__ == '__main__':
    print(get_volumes('https://ruranobe.ru/r/oregairu'))