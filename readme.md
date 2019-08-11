# Oddsportal Rugby Union Historical Odds Scraper

#### Terminal
```
python scrape.py [result-summary-url] > output.json
```

#### Output
```
{
    "Sport": "Rugby Union",
    "Season": 2019,
    "League": "Super Rugby",
    "Region": "International",
    "Games": [
        {
            "Title": "lions - jaguares",
            "Outcome": "47:39",
            "Datetime": "saturday, 09 mar 2019, 14:05",
            "Home": "lions",
            "Away": "jaguares",
            "Home Score": "47",
            "Away Score": "39",
            "Odds": [
                {
                    "Book": "18bet",
                    "Home": "1.34",
                    "Away": "3.32"
                },
                {
                    "Book": "Pinnacle",
                    "Home": "1.35",
                    "Away": "3.34"
                }
            ]
        },
        {
            "Title": "blues - sunwolves",
            "Outcome": "28:20",
            "Datetime": "saturday, 09 mar 2019, 07:35",
            "Home": "blues",
            "Away": "sunwolves",
            "Home Score": "28",
            "Away Score": "20",
            "Odds": [
                {
                    "Book": "18bet",
                    "Home": "1.12",
                    "Away": "6.42"
                },
                {
                    "Book": "Pinnacle",
                    "Home": "1.13",
                    "Away": "6.47"
                }
            ]
        }
    ],
    ...
}
```

#### Examples of result summary URLs
```
https://www.oddsportal.com/rugby-union/world/super-rugby-2016/results/
https://www.oddsportal.com/rugby-union/world/friendly-international/results/
```

## Why?
With the rugby world cup fast approaching, we are wanting to compare model predictions against historical closing lines.

Couldn't find any historical pinnacle odds for Rugby Union. 

Couldn't find any simple repositories on Github, scraping odds in general needs to be done quickly, so most were built upon Scrapy and selenium, which is overkill for this little project.

## Potential Improvements
Scraping of other markets, such as Asian Handicap, and Points totals.
All meta information stored per record for potentially easier data processing.

## Notes
- Requires Python 3.7 
- Only retrieves odds for Home/Away market (h2h) 
- H2h market includes extra time. Main desire from scraping was Pinnacle closing line.
- Requires chromium driver binary from [here](https://sites.google.com/a/chromium.org/chromedriver/home) installed relative to the script.

# Go the **All Blacks**



