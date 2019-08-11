# Oddsportal Scraper for Ruggaz!

With the Rugby world cup fast approaching, we need historical closing lines for testing prediction models. We couldn't find any historical pinnacle odds for Rugby Union. 

We also couldn't find any simple repositories on Github, scraping odds in general needs to be done quickly, most were built ontop of Scrapy, or used parallelism, which both are overkill for this little Sunday project.

May work for other sports other than Rugby Union, but has **not** been tested.

#### Terminal
```
python scrape.py [result-summary-url] > output.json
```

#### Output examples 
```
python scrape.py https://www.oddsportal.com/rugby-union/world/super-rugby/results/ > output_file.json
```

```
{
    "Sport": "Rugby Union",
    "Region": "World",
    "League": "Super Rugby",
    "Season": 2019,
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
        },
        ...
    ]
}
```

```
python scrape.py https://www.oddsportal.com/rugby-union/new-zealand/mitre-10-cup/results/ > output_file.json
```
```
{
    "Sport": "Rugby Union",
    "Region": "New Zealand",
    "League": "Mitre 10 Cup",
    "Season": "2019",
    "Games": [
        {
            "Title": "manawatu - hawke's bay",
            "Outcome": "13:31",
            "Datetime": "today, 11 aug 2019, 04:35",
            "Home": "manawatu",
            "Away": "hawke's bay",
            "Home Score": "13",
            "Away Score": "31",
            "Odds": [
                {
                    "Book": "18bet",
                    "Home": "2.29",
                    "Away": "1.62"
                },
                {
                    "Book": "Pinnacle",
                    "Home": "2.30",
                    "Away": "1.63"
                }
            ]
        },
        {
            "Title": "waikato - canterbury",
            "Outcome": "31:28",
            "Datetime": "yesterday, 10 aug 2019, 07:35",
            "Home": "waikato",
            "Away": "canterbury",
            "Home Score": "31",
            "Away Score": "28",
            "Odds": [
                {
                    "Book": "18bet",
                    "Home": "3.08",
                    "Away": "1.37"
                },
                {
                    "Book": "Pinnacle",
                    "Home": "2.80",
                    "Away": "1.45"
                }
            ]
        },
        ...
    ]
}
```

#### Other Examples of result summaries are
```
https://www.oddsportal.com/rugby-union/world/super-rugby-2016/results/
https://www.oddsportal.com/rugby-union/world/friendly-international/results/
https://www.oddsportal.com/rugby-union/japan/top-league/results/
```

#### Suggested Improvements
- Scraping of other markets, such as Asian Handicap, and Points totals.
- Create file, rather than piping output
- (Potentially) All meta information stored per record for easier data processing.
- The League / Seaon splitter is buggy for multiple year seasons. It'll be recorded as the second year. This could be resolved with a real regex but not today.

#### Notes
- Requires Python 3.7 (Probably works with 2 also)
- Only retrieves Home/Away market (h2h) odds.
- H2h market includes extra time. The goal was to get the Pinnacle odds.
- Requires chromium driver binary from [here](https://sites.google.com/a/chromium.org/chromedriver/home) installed relative to the script.


# Go the **All Blacks**
Happy Punting!
