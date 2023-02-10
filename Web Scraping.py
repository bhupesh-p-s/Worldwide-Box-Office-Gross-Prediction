import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/list/ls098063263/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

movies = []
counter = 0

while counter < 100:
    for movie in soup.find_all("div", class_="lister-item mode-detail"):
        movie_info = {}
        movie_info["name"] = movie.h3.a.text
        movie_info["genre"] = movie.find("span", class_="genre").text.strip()
        crew = []
        for tag in movie.find_all("p", class_="text-muted text-small"):
            for link in tag.find_all("a"):
                crew.append(link.text)
        if crew:
            movie_info["director"] = crew[0]
        if len(crew) > 1:
            movie_info["star_1"] = crew[1]
        if len(crew) > 2:
            movie_info["star_2"] = crew[2]
        if len(crew) > 3:
            movie_info["star_3"] = crew[3]
        if len(crew) > 4:
            movie_info["star_4"] = crew[4]
        description = movie.find("div", class_="list-description").p.b.text
        movie_info["description"] = description
        movies.append(movie_info)

    next_page = soup.find("a", class_="flat-button lister-page-next next-page")
    if not next_page:
        break

    response = requests.get("https://www.imdb.com" + next_page["href"])
    soup = BeautifulSoup(response.text, "html.parser")
    counter+=1

df = pd.DataFrame(movies)
df.to_csv("movies.csv",index=False)