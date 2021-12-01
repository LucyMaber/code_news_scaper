import requests
SPARQL_other = """

"""
SPARQL_news = """
SELECT ?news_broadcasting ?countryLabel ?official_website ?Twitter_username ?subreddit ?web_feed_URL ?Gab_username ?Media_Bias_Fact_Check_ID ?Instagram_username ?Flipboard_ID ?end_time ?AllSides_ID ?PolitiFact_people_and_groups_ID ?Google_News_publication_ID ?Snapchat_username ?Flickr_user_ID ?Giphy_username ?Reddit_username ?Quora_username ?Parler_username ?Facebook_ID ?Mastodon_address ?YouTube_channel_ID ?TikTok_username ?Quora_topic_ID ?hashtag ?Stack_Exchange_tag ?Twitter_topic_ID ?Discord_server_numeric_ID ?Wikidata_property ?language_of_work_or_name ?language_of_work_or_nameLabel ?original_language_of_film_or_TV_show ?original_language_of_film_or_TV_showLabel ?news_broadcastingLabel ?political_ideology ?political_ideologyLabel ?political_alignment ?political_alignmentLabel ?dissolved__abolished_or_demolished_date WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  { ?news_broadcasting wdt:P452 wd:Q1962634. }
  UNION
  { ?news_broadcasting wdt:P31 wd:Q11032. }
  UNION
  { ?news_broadcasting wdt:P31 wd:Q2305295. }
  UNION
  { ?news_broadcasting wdt:P31 wd:Q98785129. }
  UNION
  { ?news_broadcasting wdt:P452 wd:Q11030. }
  UNION
  { ?news_broadcasting wdt:P31 wd:Q17232649. }
  UNION
  { ?news_broadcasting wdt:P136 wd:Q19046104. }
  UNION
  { ?news_broadcasting wdt:P136 wd:Q2943864. }
  UNION
  { ?news_broadcasting wdt:P31 wd:Q11032. }
  UNION
  { ?news_broadcasting wdt:P31 wd:Q27881073. }
  UNION
  { ?news_broadcasting wdt:P6157 ?Google_News_publication_ID. }
  UNION
  { ?news_broadcasting wdt:P136 wd:Q1358344. }
  UNION
  { ?news_broadcasting wdt:P9922 ?Flipboard_ID. }
  UNION
  { ?news_broadcasting wdt:P9852 ?Media_Bias_Fact_Check_ID. }
  UNION
  { ?news_broadcasting wdt:P10006 ?AllSides_ID. }
  UNION
  { ?news_broadcasting wdt:P2267 ?PolitiFact_people_and_groups_ID. }
  UNION
  { ?news_broadcasting wdt:P6157 ?Google_News_publication_ID. }
  UNION
  {
    ?subnewspaper wdt:P279 wd:Q11032.
    ?news_broadcasting wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P279 wd:Q1153191.
    ?news_broadcasting wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P279 wd:Q28549308.
    ?news_broadcasting wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P279 wd:Q19046104.
    ?news_broadcasting wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P452 wd:Q1962634.
    ?news_broadcasting wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P31 wd:Q11032.
    ?news_broadcasting wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P31 wd:Q2305295.
    ?news_broadcasting wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P31 wd:Q98785129.
    ?news_broadcasting wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P452 wd:Q11030.
    ?news_broadcasting wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P31 wd:Q17232649.
    ?news_broadcasting wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P136 wd:Q19046104.
    ?news_broadcasting wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P136 wd:Q2943864.
    ?news_broadcasting wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P136 wd:Q11030.
    ?news_broadcasting wdt:P31 ?subnewspaper.
  }
  UNION
  { ?news_broadcasting wdt:P101 wd:Q59555084. }
  UNION
  { ?news_broadcasting wdt:P452 wd:Q59555084. }
  UNION
  { ?news_broadcasting wdt:P31 wd:Q95155801. }
  UNION
  { ?news_broadcasting wdt:P452 wd:Q95155801. }
  UNION
  { ?news_broadcasting wdt:P463 wd:Q51698517. }
  UNION
  { ?news_broadcasting wdt:P31 wd:Q28933155. }
  UNION
  { ?news_broadcasting wdt:P31 wd:Q920093. }
  { ?news_broadcasting wdt:P17 ?country. }
  { ?news_broadcasting wdt:P856 ?official_website. }
  OPTIONAL { ?news_broadcasting wdt:P1019 ?web_feed_URL. }
  MINUS { ?news_broadcasting wdt:P582 ?end_time. }
  MINUS { ?news_broadcasting wdt:P31 wd:Q13442814. }
  OPTIONAL { ?news_broadcasting wdt:P9922 ?Flipboard_ID. }
  OPTIONAL { ?news_broadcasting wdt:P9852 ?Media_Bias_Fact_Check_ID. }
  OPTIONAL { ?news_broadcasting wdt:P10006 ?AllSides_ID. }
  OPTIONAL { ?news_broadcasting wdt:P2267 ?PolitiFact_people_and_groups_ID. }
  OPTIONAL { ?news_broadcasting wdt:P6157 ?Google_News_publication_ID. }
  OPTIONAL { ?news_broadcasting wdt:P2984 ?Snapchat_username. }
  OPTIONAL { ?news_broadcasting wdt:P3267 ?Flickr_user_ID. }
  OPTIONAL { ?news_broadcasting wdt:P4013 ?Giphy_username. }
  OPTIONAL { ?news_broadcasting wdt:P4265 ?Reddit_username. }
  OPTIONAL { ?news_broadcasting wdt:P4411 ?Quora_username. }
  OPTIONAL { ?news_broadcasting wdt:P856 ?official_website. }
  OPTIONAL { ?news_broadcasting wdt:P8904 ?Parler_username. }
  OPTIONAL { ?news_broadcasting wdt:P8919 ?Gab_username. }
  OPTIONAL { ?news_broadcasting wdt:P2002 ?Twitter_username. }
  OPTIONAL { ?news_broadcasting wdt:P2013 ?Facebook_ID. }
  OPTIONAL { ?news_broadcasting wdt:P4033 ?Mastodon_address. }
  OPTIONAL { ?news_broadcasting wdt:P2397 ?YouTube_channel_ID. }
  OPTIONAL { ?news_broadcasting wdt:P7085 ?TikTok_username. }
  OPTIONAL { ?news_broadcasting wdt:P3984 ?subreddit. }
  OPTIONAL { ?news_broadcasting wdt:P856 ?official_website. }
  OPTIONAL { ?news_broadcasting wdt:P6157 ?Google_News_publication_ID. }
  OPTIONAL { ?news_broadcasting wdt:P856 ?official_website. }
  OPTIONAL { ?news_broadcasting wdt:P3417 ?Quora_topic_ID. }
  OPTIONAL { ?news_broadcasting wdt:P2572 ?hashtag. }
  OPTIONAL { ?news_broadcasting wdt:P1482 ?Stack_Exchange_tag. }
  OPTIONAL { ?news_broadcasting wdt:P8672 ?Twitter_topic_ID. }
  OPTIONAL { ?news_broadcasting wdt:P9345 ?Discord_server_numeric_ID. }
  OPTIONAL { ?news_broadcasting wdt:P1687 ?Wikidata_property. }
  OPTIONAL { ?news_broadcasting wdt:P407 ?language_of_work_or_name. }
  OPTIONAL { ?news_broadcasting wdt:P364 ?original_language_of_film_or_TV_show. }
  OPTIONAL { ?news_broadcasting wdt:P1142 ?political_ideology. }
  OPTIONAL { ?news_broadcasting wdt:P1387 ?political_alignment. }
  MINUS { ?news_broadcasting wdt:P576 ?dissolved__abolished_or_demolished_date. }
  MINUS { ?news_broadcasting wdt:P582 ?end_time. }
}
"""
class SPRQL:
    def  __init__(self,sparql,url) -> None:
        self.sparql = sparql
        self.url = url
    def  run(self) -> None:
        da = {}
        #print(self.url)
        r = requests.get(self.url, params = {'format': 'json', 'query': self.sparql})
        data = r.json()
        for i in data["results"]["bindings"]:
            if i["news_broadcasting"]["value"] not in da.keys():
                da[i["news_broadcasting"]["value"]] = {}
            for ke in i.keys():
                if not ke in da[i["news_broadcasting"]["value"]].keys():
                  da[i["news_broadcasting"]["value"]][ke] = []
                if i[ke]["value"] not in da[i["news_broadcasting"]["value"]][ke]:
                  da[i["news_broadcasting"]["value"]][ke].append(i[ke]["value"])
        return  da