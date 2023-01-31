# TODO: scrap the website "https://www.adamchoi.co.uk/overs/detailed"
# (1) click on the "all matches" button
#       - locate the button through xpath (find by xpath in developer tool & make sure the xpath only match one elements, to ensure it is a solid way to locate )
# (2) scrap data from table
#       - access the table row by row (hint: tr tag)
#       - save the data from each row to 4 separate list: date, home_team, score, away_team (hint: td tag)
# (3) export data to csv file with pandas
# (4) select country within dropdown as "Spain" 
#       - pause the execution of code for 3 seconds to prevent Selenium's "TimeoutException" during

#%%
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

webpage = "https://www.adamchoi.co.uk/overs/detailed"
path_webdriver = '../webdriver_for_webscraping/chromedriver_mac_arm64/chromedriver'
# initialize a Chrome webdriver
driver = webdriver.Chrome(path_webdriver)
# Load the webpage in a new browser window.
driver.get(webpage)

# locate "all matches" button
all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

#%%
# locate "country" dropbox
country_dropbox = Select(driver.find_element_by_xpath('//select[@id="country"]'))
country_dropbox.select_by_visible_text("Spain")

# pause the execution of code for 3 seconds
time.sleep(3)

# scrap table 
date_list = []
home_list = []
score_list = []
away_list = []
for row in driver.find_elements_by_tag_name('tr'):
    date = row.find_element_by_xpath('./td[1]').text
    date_list.append(date)
    home = row.find_element_by_xpath('./td[2]').text
    home_list.append(home)
    score = row.find_element_by_xpath('./td[3]').text
    score_list.append(score)
    away = row.find_element_by_xpath('./td[4]').text
    away_list.append(away)
    
#%%
# store table contents as a pandas dataframe
df = pd.DataFrame(data= {"date":date_list, "home_team":home_list, "score":score_list, "away_team":away_list})
df.to_csv("football_data.csv", index=False)

# %%
# turn off the Chrome webdriver (an important step!!)
driver.quit()

# %%
