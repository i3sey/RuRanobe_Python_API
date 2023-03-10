import requests
from bs4 import BeautifulSoup as bs

def get_desc(link):
    r = requests.get(link)
    soup = bs(r.text, "html.parser")
    return soup.find_all('div', class_ = 'info__annotation')[0].text.replace('\n', '') 

if __name__ == '__main__':
    print(get_desc('https://ruranobe.ru/r/oregairu'))