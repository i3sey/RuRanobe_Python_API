import requests
from bs4 import BeautifulSoup as bs


def get_names(link):
    r = requests.get(link)
    soup = bs(r.text, "html.parser")
    return f"{soup.find_all('span', class_ = 'headline__text')[0].text}{soup.find_all('app-alt-names')[0].text.replace('Японское: ', '/').replace(' Английское: ', '/').replace(' Ромадзи: ', '/')}"


if __name__ == '__main__':
    print(get_names('https://ruranobe.ru/r/tnynn'))
