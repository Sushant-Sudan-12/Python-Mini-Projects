import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website,"html.parser")

all_movies = soup.find_all(name="h3")
print(all_movies)

