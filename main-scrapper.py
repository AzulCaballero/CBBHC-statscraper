from bs4 import BeautifulSoup
import requests
import pandas as pd

# Process 1: Fetch game page URLs from game center
gc_url = 'http://cfbhc.com/index.php?/forum/575-game-center/page/1/'
gc_page = requests.get(gc_url).text
gc_soup = BeautifulSoup(gc_page, 'lxml')

gamelist = []
for threads in gc_soup.find_all('a', attrs={'data-ipshover-timeout': '1.5'}):
   rows = threads.get('href')
   gamelist.append(rows)

del gamelist[0]

# Process 2: Open data spreadsheet

# Process 3: Let's stugglebus through some games for raw data
raw = []

for game in gamelist:
    url = requests.get(game).text
    soup = BeautifulSoup(url, 'lxml')

    row = []
    tables = soup.find_all('table', attrs={'class': 'boxscore'})

    for table in tables:
        boxes = table.find_all('tr')

        for box in boxes:
            cols = box.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            if len(cols) > 0:
                x = cols[0]
            row.append([ele for ele in cols if ele])

raw = [i for i in raw if i[0]!='']
dataset = pd.DataFrame(row)

dataset.to_csv("Dataset.csv", index = False)

print("fuck ya")