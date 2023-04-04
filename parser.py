from bs4 import BeautifulSoup
import requests

def Parse():
    BaseUrl = "https://www.omgtu.ru/l/?PAGEN_1={}"
    file = open("output.txt", "w", encoding='utf-8')
    for PageNumber in range(1, 158):
        url = BaseUrl.format(PageNumber)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        block = soup.findAll('h3', class_='news-card__title')
        for data in block:
            description = data.text
            file.write(description.strip() + "\n")
    file.close()
