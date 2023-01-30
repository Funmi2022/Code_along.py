# https://www.datamann.com/bills-blog
import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://www.datamann.com/bills-blog")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article") 
print(articles) 
