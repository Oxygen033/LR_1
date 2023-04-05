from bs4 import BeautifulSoup
import requests

def FileWrite(str):
    file = open("output.txt", "w", encoding='utf-8')
    file.write(str)
    file.close()

def Parse():
    baseUrl = "https://www.omgtu.ru/l/?PAGEN_1={}"
    for pageNumber in range(1, 158):
        url = baseUrl.format(pageNumber)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        block = soup.findAll('h3', class_='news-card__title')
        for data in block:
            description = data.text
            FileWrite(description.strip() + "\n")
    file.close()

