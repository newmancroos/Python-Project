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
