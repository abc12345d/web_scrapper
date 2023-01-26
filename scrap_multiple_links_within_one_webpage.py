# scrap the links appear in the below webpage 
# https://subslikescript.com/movies
# visit each link 
# store the link title as filename and transcript as file content

#%%
import requests
from bs4 import BeautifulSoup 

#%%
# Extracting the links of multiple movie transcripts
#####################################################

# get the html 
root = "https://subslikescript.com/"
website = requests.get(root+"movies")
# parse the html file with "lxml" parser into a  BeautifulSoup object
soup = BeautifulSoup(website.text,"lxml")

# locate the box that contains a list of links
scripts_list = soup.find(class_="scripts-list").findAll("a",href=True)
# extract the links 
links_list = [a['href'] for a in scripts_list]


#%%
# Extracting the movie transcript
#################################################

# loop through the list of links and send request to each link
for link in links_list:
    movie_page = requests.get(root+link)
    movie_soup = BeautifulSoup(movie_page.text,"lxml")

    # locate and get the title of movie
    title = movie_soup.find("h1").text
    # locate and get the transcript of movie
    scripts = movie_soup.find(class_="full-script").get_text(separator=" ",strip=True)

    # export transcripts to a txt file with the title as the filename
    with open(title+'.txt','w') as file:
        file.write(scripts)
