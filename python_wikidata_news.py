## https://www.worldometers.info/geography/alphabetical-list-of-countries/
## USA
US_news = """
SELECT DISTINCT ?newspaper ?newspaperLabel ?end_time WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  ?newspaper wdt:P17 wd:Q30.
  { ?newspaper wdt:P31 wd:Q11032. }
  UNION
  { ?newspaper wdt:P31 wd:Q2305295. }
  UNION
  { ?newspaper wdt:P31 wd:Q98785129. }
  UNION
  { ?newspaper wdt:P452 wd:Q1962634. }
  UNION
  { ?newspaper wdt:P31 wd:Q1153191. }
  UNION
  { ?newspaper wdt:P31 wd:Q66693223. }
  UNION
  { ?newspaper wdt:P452 wd:Q11030. }
  UNION
  { ?newspaper wdt:P101 wd:Q11030. }
  { ?newspaper wdt:P856 ?official_website. }
  FILTER(!(REGEX(STR(?official_website), "[a-z]/[a-z?]")))
  MINUS { ?newspaper wdt:P582 ?end_time. }
}
"""