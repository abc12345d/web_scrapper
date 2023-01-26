#%%
from bs4 import BeautifulSoup
import requests

webpage = 'https://subslikescript.com/series/Friends-108778/season-1/episode-1-The_One_Where_Monica_Gets_a_Roommate'
response = requests.get(webpage)

# %%
html_content = response.text
soup = BeautifulSoup(html_content,'lxml')

# print the html content in a pretty way
# print(soup.prettify())
# %%
# Locate the box that contains title and transcript
box = soup.find('article',class_='main-article')
# Locate title and transcript
title = box.find('h1').get_text()
transcript = box.find('div',class_="full-script").get_text(strip=True, separator=' ')
# %%
# Exporting data in a text file with the "title" name
with open(title+'.txt','w') as file:
    file.write(title +'\n')
    file.write(transcript)
# %%
