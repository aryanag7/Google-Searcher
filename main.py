import requests , webbrowser
from bs4 import BeautifulSoup

user = input("What do you want to search? ")
print("Searching....")
req = requests.get("https://www.google.com/search?q="+user)
soup = BeautifulSoup(req.text,'lxml')
search = soup.select('.kCrYT a')

for i in search[:5]:
    new_search = i.get("href")
    webbrowser.open("https://www.google.com/"+new_search)
