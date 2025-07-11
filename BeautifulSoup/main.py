import requests
from bs4 import BeautifulSoup

url="https://news.ycombinator.com/news"

response= requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

article_texts=[]
article_links=[]

articles = soup.select(selector=".title .titleline a")
for article in articles:
    article_text = article.getText()
    article_link = article.get("href")
    article_texts.append(article_text)
    article_links.append(article_link)


# article_apvotes =soup.find_all(name="span", class_="score")
# article_apvotess=[]
# for apvote in article_apvotes:
#     article_apvotess.append(apvote.getText())
# print(article_apvotess)

article_apvotess=[int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

larget_number= max(article_apvotess)
large_index=article_apvotess.index(larget_number)

print(article_texts)
print(article_links)
print(article_apvotess)


