from bs4 import BeautifulSoup as bs4
import requests
url = "https://lite.cnn.com/en/article/h_6abe87c2bd1ce0407900d1fe6ad10805"
text = requests.get(url).text
soup = bs4(text,"html.parser")
print(soup)