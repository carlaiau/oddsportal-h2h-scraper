#Importing packages
from selenium import webdriver
import json
import re
import sys
from datetime import datetime

# Get Meta information from original page
def get_tournament_data(driver):
    breadcrumb = driver.find_elements_by_xpath("//div[@id='breadcrumb']//a")
    league = breadcrumb[3].text
    year = datetime.now().strftime('%Y')

    splitLeague = re.split(' 2015| 2016| 2017| 2018| 2019', league)
    if(len(splitLeague) > 1):
        league = splitLeague[0]
        year = breadcrumb[3].text[-4:]

    return {
        "Sport": breadcrumb[1].text,
        "Region": breadcrumb[2].text,
        "League": league,
        "Season": year,
        "Games": []
    }

# Get the pagination from the intial page, 
# and create a unique list of the other pages from the same season
def get_pages(d):
    urls = []
    links = d.find_elements_by_xpath("//div[@id='pagination']//a")
    for l in links:
        urls.append(l.get_attribute('href'))
    return  [x for i, x in enumerate(urls) if i == urls.index(x)] # return unique list

# Get games from result overview URL
def get_games(d, urls):
    games = []
    for url in urls:
        d.get(url)
        links = d.find_elements_by_xpath(
            "//table[@id='tournamentTable']//tr[@class='odd deactivate']//td[@class='name table-participant']//a")
        for l in links:
            games.append(l.get_attribute('href'))
    return games


# Get odds from one specific game url
def get_odds(d, url):
    d.get(url)
    d.find_element_by_xpath("//div[@id='bettype-tabs']//*[text()=('Home/Away')]").click()
    d.find_element_by_xpath("//div[@id='bettype-tabs-scope']//ul[2]/li[1]").click()

    title = d.find_element_by_xpath("//div[@id='col-content']//h1").text
    h_name = title.split(" - ")[0]
    a_name = title.split(" - ")[1]

    score = d.find_element_by_xpath("//div[@id='event-status']//p//strong").text
    h_score = score.split(":")[0]
    a_score = score.split(":")[1]

    datetime  = d.find_element_by_xpath("//p[contains(@class, 'date datet')]").text

    rows = d.find_elements_by_xpath(
        "//div[@id='odds-data-table']//table[contains(@class,'table-main')]//tbody//tr[contains(@class,'lo')]")
    
    odds = []
    for row in rows:
        bookmaker_name = row.find_element_by_xpath(".//a[@class='name']").text
        tds = row.find_elements_by_xpath(".//td[contains(@class, 'odds')]")
        odd = {
            "Book" : bookmaker_name,
            "Home": tds[0].text,
            "Away": tds[1].text
        }
        odds.append(odd)
    return {
        "Title": title.lower(),
        "Outcome": score,
        "Datetime": datetime.lower(),
        "Home": h_name.lower(),
        "Away": a_name.lower(),
        "Home Score": h_score,
        "Away Score": a_score,
        "Odds": odds
    }

# Main Thread!  
def main(url):
    driver = webdriver.Chrome('./chromedriver') ## Change this if chromedriver is somewhere else
    driver.implicitly_wait(10) # Shitty Oddsportal AJAX table load ins
    driver.get(url)
    results = get_tournament_data(driver)
    
    pages = get_pages(driver)
    if(len(pages) == 0 ): # Has no breadcrumb, only one page of results
        pages = [url]

    for game in get_games(driver, pages):
        results["Games"].append(get_odds(driver, game))

    driver.close()
    print(json.dumps(results))    

## Run this!
if(len(sys.argv) < 2):
    print("\nRemember this requires URL!:\npython scrape.py https://oddsportal.com/rugby-result-url > output.json\n")
else:
    main(sys.argv[1])


