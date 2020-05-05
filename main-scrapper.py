from bs4 import BeautifulSoup
import requests

# Process 1: Fetch raw HTML from a URL
url = "http://cfbhc.com/index.php?/topic/31964-2024-reg-florida-gators-0-0-at-xavier-musketeers-0-0/"
page = requests.get(url).text

# Process 2: Parse the html content
soup = BeautifulSoup(page, "lxml")
# print(soup.prettify()) # print the parsed data of html

# Process 3: Extract game title to identify game
game = soup.title.string.replace(' - Game Center - College Football Head Coach', '')
print(game)

boxscore = soup.find("table", attrs={"class": "boxscore"})
boxscore_data = boxscore.find_all('tr')

for tr in boxscore_data:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row[0])
