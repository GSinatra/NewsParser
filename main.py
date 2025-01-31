import requests
from bs4 import BeautifulSoup

url = "https://lenta.ru"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

# title = soup.title.text
# print(title)

links = [a.get("href") for a in soup.find_all("a") if "card-mini__title" in a.get("href")]
for i in soup.find_all("h3"):
    print(i)
