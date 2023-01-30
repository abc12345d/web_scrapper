# TODO: scrap the website "https://www.adamchoi.co.uk/overs/detailed"
# (1) click on the "all matches" button
#       - locate the button through xpath (find by xpath in developer tool & make sure the xpath only match one elements, to ensure it is a solid way to locate )
# (2) scrap data from table
#       - access the table row by row (hint: tr tag)
#       - save the data from each row to 4 separate list: date, home_team, score, away_team (hint: td tag)
# (3) export data to csv file with pandas
# (4) select country within dropdown as "Spain" 
#       - pause the execution of code for 3 seconds to prevent Selenium's "TimeoutException" during

