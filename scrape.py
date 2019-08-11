#Importing packages
from selenium import webdriver
import json
import re
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
def get_pages(driver):
    urls = []
    linkElements = driver.find_elements_by_xpath("//div[@id='pagination']//a")

    for link in linkElements:
        urls.append(link.get_attribute('href'))
    return  [x for i, x in enumerate(urls) if i == urls.index(x)] # return unique list

# Get games from result overview URL
def get_games(driver, urls):
    games = []
    for url in urls:
        driver.get(url)
        gameLinks = driver.find_elements_by_xpath(
            "//table[@id='tournamentTable']//tr[@class='odd deactivate']//td[@class='name table-participant']//a")
        for link in gameLinks:
            games.append(link.get_attribute('href'))
    return games


# Get odds from one specific game url
def get_odds(driver, url):
    driver.get(url)
    driver.find_element_by_xpath("//div[@id='bettype-tabs']//*[text()=('Home/Away')]").click()
    driver.find_element_by_xpath("//div[@id='bettype-tabs-scope']//ul[2]/li[1]").click()

    title = driver.find_element_by_xpath("//div[@id='col-content']//h1").text
    home_team = title.split(" - ")[0]
    away_team = title.split(" - ")[1]

    score = driver.find_element_by_xpath("//div[@id='event-status']//p//strong").text
    home_score = score.split(":")[0]
    away_score = score.split(":")[1]

    datetime  = driver.find_element_by_xpath("//p[contains(@class, 'date datet')]").text

    rows = driver.find_elements_by_xpath(
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
        "Home": home_team.lower(),
        "Away": away_team.lower(),
        "Home Score": home_score,
        "Away Score": away_score,
        "Odds": odds
    }

def main():
    driver = webdriver.Chrome('./chromedriver')    
    driver.implicitly_wait(10)
    driver.get('https://www.oddsportal.com/rugby-union/world/super-rugby-2018/results/')
    results = get_tournament_data(driver)

    for game in get_games(driver, get_pages(driver)):
        results["Games"].append(get_odds(driver, game))

    driver.close()
    print(json.dumps(results))    

# Main Thread!    
main()
