#Importing packages
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('chromedriver/chromedriver')
driver.implicitly_wait(10)


def get_games():

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

def get_odds(url):
    driver.get(url)
    driver.find_element_by_xpath("//div[@id='bettype-tabs']//*[text()=('Home/Away')]").click()
    driver.find_element_by_xpath("//div[@id='bettype-tabs-scope']//ul[2]/li[1]").click()
    rows = driver.find_elements_by_xpath("//div[@id='odds-data-table']//table[contains(@class,'table-main')]//tbody//tr[contains(@class,'lo')]")

    for row in rows:
        bookmaker_name = row.find_element_by_xpath(".//a[@class='name']").text
        odds = row.find_elements_by_xpath(".//td[contains(@class, 'odds')]")
        home_odd = odds[0].text
        away_odd = odds[1].text
        print(bookmaker_name)
        print(home_odd)
        print(away_odd)



one_game = "https://www.oddsportal.com/rugby-union/world/super-rugby/golden-lions-jaguares-vVL1AYLS/"
get_odds(one_game)
driver.close()