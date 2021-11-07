from SPARQLWrapper import SPARQLWrapper, JSON

def newsDataQurry():
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
    qaurry ="""
    SELECT ?news_broadcasting ?news_broadcastingLabel ?Facebook_ID ?Instagram_username ?Media_Bias_Fact_Check_ID ?Quora_topic_ID ?Twitter_username ?YouTube_channel_ID ?Twitter_user_numeric_ID ?Twitter_topic_ID ?tweet_ID ?Gab_username ?Parler_username ?subreddit ?Reddit_username ?Myspace_ID ?political_alignment ?political_alignmentLabel ?political_ideology ?political_ideologyLabel ?language_used ?language_usedLabel ?official_website WHERE {
      SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
      #{ ?news_broadcasting wdt:P452 wd:Q1962634. }
      #UNION
      #{ ?news_broadcasting wdt:P452 wd:Q11030. }
      #UNION
      #{ ?news_broadcasting wdt:P31 wd:Q1110794. }
      #UNION
      #{ ?news_broadcasting wdt:P31 wd:Q11032. }
      #UNION
      #{ ?news_broadcasting wdt:P31 wd:Q2305295. }
      #UNION
      #{ ?news_broadcasting wdt:P31 wd:Q98785129. }
      #UNION
      #{ ?news_broadcasting wdt:P31 wd:Q106651350. }
      #UNION
      #{ ?news_broadcasting wdt:P452 wd:Q1539062. }
      #UNION
      { ?news_broadcasting wdt:P31 wd:Q1153191. }
      UNION
      { ?news_broadcasting wdt:P31 wd:Q17232649. }
      OPTIONAL { ?news_broadcasting wdt:P2013 ?Facebook_ID. }
      OPTIONAL { ?news_broadcasting wdt:P2003 ?Instagram_username. }
      OPTIONAL { ?news_broadcasting wdt:P9852 ?Media_Bias_Fact_Check_ID. }
      OPTIONAL { ?news_broadcasting wdt:P3417 ?Quora_topic_ID. }
      OPTIONAL { ?news_broadcasting wdt:P2002 ?Twitter_username. }
      OPTIONAL { ?news_broadcasting wdt:P2397 ?YouTube_channel_ID. }
      OPTIONAL { ?news_broadcasting wdt:P2002 ?Twitter_username. }
      OPTIONAL { ?news_broadcasting wdt:P6552 ?Twitter_user_numeric_ID. }
      OPTIONAL { ?news_broadcasting wdt:P8672 ?Twitter_topic_ID. }
      OPTIONAL { ?news_broadcasting wdt:P5933 ?tweet_ID. }
      OPTIONAL { ?news_broadcasting wdt:P8919 ?Gab_username. }
      OPTIONAL { ?news_broadcasting wdt:P8904 ?Parler_username. }
      OPTIONAL { ?news_broadcasting wdt:P3984 ?subreddit. }
      OPTIONAL { ?news_broadcasting wdt:P4265 ?Reddit_username. }
      OPTIONAL { ?news_broadcasting wdt:P3265 ?Myspace_ID. }
      OPTIONAL { ?news_broadcasting wdt:P1387 ?political_alignment. }
      OPTIONAL { ?news_broadcasting wdt:P1142 ?political_ideology. }
      OPTIONAL { ?news_broadcasting wdt:P2936 ?language_used. }
      OPTIONAL { ?news_broadcasting wdt:P3417 ?Quora_topic_ID. }
      OPTIONAL { ?news_broadcasting wdt:P856 ?official_website. }
    }
    """
    sparql.setReturnFormat(JSON)
    sparql.setQuery(qaurry)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print(result)
newsDataQurry()

"""
SELECT DISTINCT ?itemLabel WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  { ?item wdt:P101 ?field_of_work. }
  UNION
  { ?item wdt:P2650 ?field_of_work. }
  UNION
  { ?item wdt:P1142 ?field_of_work. }
  { ?item wdt:P17 wd:Q145. }
  UNION
  { ?item wdt:P495 wd:Q145. }
  UNION
  {
  minus { ?item wdt:P17 ?c. }
  minus { ?item wdt:P495 ?c. }
  }

  MINUS { ?item wdt:P31 wd:Q5. }
  { ?item wdt:P856 ?official_website. }
  UNION
  { ?item wdt:P1019 ?web_feed_URL. }
  MINUS { ?item wdt:P1433 wd:Q66693223. }
  MINUS { ?item wdt:P31 wd:Q11032. }
  MINUS { ?item wdt:P31 wd:Q2305295. }
  MINUS { ?item wdt:P31 wd:Q1110794. }
  MINUS { ?item wdt:P31 wd:Q98785129. }
  MINUS { ?item wdt:P452 wd:Q1962634. }
  MINUS { ?item wdt:P452 wd:Q11030. }
  MINUS { ?item wdt:P31 wd:Q27881073. }
}
"""