# locate the pagination class in the below link
# https://subslikescript.com/movies_letter-A
# visit all the links to different webpages of the website
# visit all the links to different movies within each webpage
# store the movie title as filename and movie transcript as file content

#%%
from bs4 import BeautifulSoup
import requests

# %%
# extract the links to different webpages of the website
############################################################

root = "https://subslikescript.com/"
website = requests.get(f"{root}movies_letter-A")
soup = BeautifulSoup(website.text,"lxml")

# locate the pagination class 
pagination = soup.find(class_="pagination")
# find the last webpage number of this section https://subslikescript.com/movies_letter-A
last_no = int(pagination.findAll(class_="page-link",href=True,rel=False)[-1].text)

#%%
# visit all the webpages of this section https://subslikescript.com/movies_letter-A
for page in range(1,last_no+1):

    webpage = requests.get(f'{root}movies_letter-A?page={str(page)}')
    webpage_soup = BeautifulSoup(webpage.text,"lxml")
    # get links to movie transcript from each webpage
    movie_link_list = [a["href"] for a in webpage_soup.find(class_="scripts-list").findAll(href=True)]

    # visit all the links to movie transcript within each webpage
    # store the movie title as filename and movie transcript as file content
    for movie_link in movie_link_list:
        movie_page = requests.get(f"{root}{movie_link}")
        movie_soup = BeautifulSoup(movie_page.text,"lxml")

        title = movie_soup.find("h1").text
        transcript = movie_soup.find(class_="full-script").get_text(separator=" ",strip=True)

        with open(f"{title}.txt","w") as file:
            
            file.write(transcript)