import requests
from bs4 import BeautifulSoup as bs

github_user = input("Enter Github Username:")

url = "https://www.github.com/"+github_user
r = requests.get(url)
content_page = bs(r.content, 'html.parser')
profile_picture = content_page.find('img', {'alt': 'Avatar'})['src']

print(profile_picture)