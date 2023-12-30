import pandas as pd
import requests as requests
from bs4 import BeautifulSoup
web_url = "https://parsehub.com/sandbox/showtimes"
fetched_page = requests.get(web_url)

#print(fetched_page.text)

beautifulsoup = BeautifulSoup(fetched_page.text,"html.parser")

titles = []
urls = []
time = []

for movie in beautifulsoup.find_all('a','title'):
 titles.append(movie.string)
 urls.append(movie.get('href'))
 # print(movie.string)
 # print(movie.get('href'))

for showtime in beautifulsoup.find_all('span','imax'):
 time.append(showtime.string)
 # print(showtime.string)

raw_data={
 'movie_title':titles,
 'show_time':time,
 'image_url':urls
}

dataframe = pd.DataFrame(raw_data, columns=['movie_title', 'show_time', 'image_url'])
dataframe.to_csv('raw_data.csv', index=False)
print(dataframe)