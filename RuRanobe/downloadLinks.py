from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def downloadLinks(link):
    # driver = webdriver.Chrome()
    # driver.get(link)
    # element = driver.find_element(By.XPATH, "/html/body/app-root/app-theme/div[1]/app-layout/main/div/app-project/section/div/div/div[2]/div[2]/div/app-volume-download/button")
    # ActionChains(driver).click(element).perform()
    # pass
    r = requests.get(link)
    soup = bs(r.text, "html.parser")
    links = {}
    new_var = soup.find_all('div', class_ = 'download__buttons')
    for form in new_var:
        for an in form:
            links.update({an.text:f"https://ruranobe.ru{an['href']}"})
    return links
    
print(downloadLinks('https://ruranobe.ru/r/tnynn/v1'))