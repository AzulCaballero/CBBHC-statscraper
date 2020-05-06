from bs4 import BeautifulSoup
import requests
import csv

# Process 1: Fetch raw HTML from a URL
url = 'http://cfbhc.com/index.php?/topic/31964-2024-reg-florida-gators-0-0-at-xavier-musketeers-0-0/'
page = requests.get(url).text

# Process 2: Parse the html content
soup = BeautifulSoup(page, 'lxml')
# print(soup.prettify()) # print the parsed data of html

# Process 3: Extract game title to identify game
game = soup.title.string.replace(' - Game Center - College Football Head Coach', '')
print(game)

data = []
table = soup.find_all('table', attrs={'class': 'boxscore'})
print(table)
box = table.find_all('tbody')

rows = box.find_all("tr")
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

# open csv
csvfile = open('cbbtest.csv', 'w')
writer = csv.writer(csvfile)
writer.writerow(data)

# close csv
csvfile.close()
