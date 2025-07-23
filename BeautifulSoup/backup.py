from bs4 import BeautifulSoup
import  lxml   #this package for parsing xml

with open("website.html", "r") as file:
    content = file.read()

soup = BeautifulSoup(content,'html.parser') #lxml  -> for xml
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a)   #Print first  a tag
# #print(soup.prettify())  #Nicely indented format

#Find All
all_a = soup.find_all(name="a") #get all tags with the given name
print(all_a)

for tag in all_a:
    # print(tag.getText())  #tag.string also works
    print(tag.get("href")) #get parameter value

heading = soup.find(name="h1", id="name")
print(heading)

by_class =soup.find(name="h3", class_="heading")
print(by_class.getText())
print(by_class.get("class"))

#if we want to find a a tag with in another tag

company_url = soup.select_one(selector="p em strong a") # p a is enough
print(company_url)

my_name = soup.select_one(selector="#name") # by Id
print(my_name)

other_page = soup.select_one(selector=".heading")  #by class
print(other_page)
#----------------------------------
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


