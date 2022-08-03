from bs4 import BeautifulSoup
import requests

def find_max_index(list):
    maximum = max(list)
    index = list.index(maximum)
    return index

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")
titles = soup.find_all(name="h3", class_="title")

with open("100_Movies.txt", "w", encoding="utf-8") as content:
    for item in titles[::-1]:
        text = item.getText()
        content.write(f"{text}, \n")