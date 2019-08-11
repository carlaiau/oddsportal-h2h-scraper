#Importing packages
from selenium import webdriver
import pandas as pd
import json

# Get games from result overview URL
def get_games(driver):
    games = []
    super15 = [
        'https://www.oddsportal.com/rugby-union/world/super-rugby/results/#/page/3/',
        'https://www.oddsportal.com/rugby-union/world/super-rugby/results/#/page/2/',
        'https://www.oddsportal.com/rugby-union/world/super-rugby/results/'
    ]
    for l in super15:
        driver.get(l)
        gameLinks = driver.find_elements_by_xpath("//table[@id='tournamentTable']//tr[@class='odd deactivate']//td[@class='name table-participant']//a")
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

    rows = driver.find_elements_by_xpath("//div[@id='odds-data-table']//table[contains(@class,'table-main')]//tbody//tr[contains(@class,'lo')]")
    
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

results = {
    "Sport": "Rugby Union",
    "Season": 2019,
    "League": "Super Rugby",
    "Region": "International" ,
    "Games": []
}


def main():
    driver = webdriver.Chrome('chromedriver/chromedriver')
    driver.implicitly_wait(10)
    
    for game in get_games(driver):
        results["Games"].append(get_odds(driver, game))
    
    print(json.dumps(results))
    
    driver.close()



# run!
main()
