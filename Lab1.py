from bs4 import BeautifulSoup
import requests

url = "https://www.omgtu.ru"
page= requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
file = open("output.txt", "w")
while True:
    block = soup.findAll('h3', class_='news-card__title')
    description = ''
    for data in block:
        description = data.text
        file.write(description)
    break
file.close()
