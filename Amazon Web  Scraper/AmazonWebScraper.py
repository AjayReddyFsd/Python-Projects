import requests
from bs4 import BeautifulSoup
import datetime  # to add timestamps to the csv file whenever a data is added to it


def AmazonWebScraper():
    # userInput = input('Hey there! What do you wanna search today in Amazon: ').lower().replace(' ', '+')
    # URL = 'https://www.amazon.ca/s?k=' + userInput

    URL = 'https://www.amazon.ca/External-Drive%EF%BC%8CExternal-Desktop-MacBook-Chromebook/dp/B0BG1DKDSQ/ref=sr_1_1_sspa?keywords=electronics&qid=1666808003&qu=eyJxc2MiOiI4LjkxIiwicXNhIjoiOC4xNiIsInFzcCI6IjYuOTQifQ%3D%3D&sr=8-1-spons&psc=1'
    webPage = requests.get(URL)
    soup = BeautifulSoup(webPage.content, "html.parser").prettify()

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Host": "httpbin.org",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
        "X-Amzn-Trace-Id": "Root=1-63597d58-104886874de5ea841c4b1094"
    }

    title = soup.find(id='productTitle').get_Text()
    print(title)


AmazonWebScraper()
