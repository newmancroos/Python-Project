import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response=requests.get(URL)
content = BeautifulSoup(response.text, "html.parser")
# print(content)
movie_content = content.find_all(name="h3", class_="title")
movie_list = [movie.getText() for movie in movie_content]
# movie_list.reverse()
movie_list = movie_list[::-1]

with open("movie_list.txt","w", encoding='utf-8') as file:
    for movie in movie_list:
        file.write(f"{movie}\n")

