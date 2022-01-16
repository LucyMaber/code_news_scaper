from time import sleep
import requests
SPARQL_other = """

"""
SPARQL_news = """
SELECT ?Thing ?countryLabel ?official_website ?Twitter_username ?subreddit ?web_feed_URL ?Gab_username ?Media_Bias_Fact_Check_ID ?Instagram_username ?Flipboard_ID ?end_time ?AllSides_ID ?PolitiFact_people_and_groups_ID ?Google_News_publication_ID ?Snapchat_username ?Flickr_user_ID ?Giphy_username ?Reddit_username ?Quora_username ?Parler_username ?Facebook_ID ?Mastodon_address ?YouTube_channel_ID ?TikTok_username ?Quora_topic_ID ?hashtag ?Stack_Exchange_tag ?Twitter_topic_ID ?Discord_server_numeric_ID ?Wikidata_property ?language_of_work_or_name ?language_of_work_or_nameLabel ?original_language_of_film_or_TV_show ?original_language_of_film_or_TV_showLabel ?ThingLabel ?political_ideology ?political_ideologyLabel ?political_alignment ?political_alignmentLabel ?dissolved__abolished_or_demolished_date WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  { ?Thing wdt:P452 wd:Q1962634. }
  UNION
  { ?Thing wdt:P31 wd:Q11032. }
  UNION
  { ?Thing wdt:P31 wd:Q2305295. }
  UNION
  { ?Thing wdt:P31 wd:Q98785129. }
  UNION
  { ?Thing wdt:P452 wd:Q11030. }
  UNION
  { ?Thing wdt:P31 wd:Q17232649. }
  UNION
  { ?Thing wdt:P136 wd:Q19046104. }
  UNION
  { ?Thing wdt:P136 wd:Q2943864. }
  UNION
  { ?Thing wdt:P31 wd:Q11032. }
  UNION
  { ?Thing wdt:P31 wd:Q27881073. }
  UNION
  { ?Thing wdt:P6157 ?Google_News_publication_ID. }
  UNION
  { ?Thing wdt:P136 wd:Q1358344. }
  UNION
  { ?Thing wdt:P9922 ?Flipboard_ID. }
  UNION
  { ?Thing wdt:P9852 ?Media_Bias_Fact_Check_ID. }
  UNION
  { ?Thing wdt:P10006 ?AllSides_ID. }
  UNION
  { ?Thing wdt:P2267 ?PolitiFact_people_and_groups_ID. }
  UNION
  { ?Thing wdt:P6157 ?Google_News_publication_ID. }
  UNION
  {
    ?subnewspaper wdt:P279 wd:Q11032.
    ?Thing wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P279 wd:Q1153191.
    ?Thing wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P279 wd:Q28549308.
    ?Thing wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P279 wd:Q19046104.
    ?Thing wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P452 wd:Q1962634.
    ?Thing wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P31 wd:Q11032.
    ?Thing wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P31 wd:Q2305295.
    ?Thing wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P31 wd:Q98785129.
    ?Thing wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P452 wd:Q11030.
    ?Thing wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P31 wd:Q17232649.
    ?Thing wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P136 wd:Q19046104.
    ?Thing wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P136 wd:Q2943864.
    ?Thing wdt:P31 ?subnewspaper.
  }
  UNION
  {
    ?subnewspaper wdt:P136 wd:Q11030.
    ?Thing wdt:P31 ?subnewspaper.
  }
  UNION
  { ?Thing wdt:P101 wd:Q59555084. }
  UNION
  { ?Thing wdt:P452 wd:Q59555084. }
  UNION
  { ?Thing wdt:P31 wd:Q95155801. }
  UNION
  { ?Thing wdt:P452 wd:Q95155801. }
  UNION
  { ?Thing wdt:P463 wd:Q51698517. }
  UNION
  { ?Thing wdt:P31 wd:Q28933155. }
  UNION
  { ?Thing wdt:P31 wd:Q920093. }
  { ?Thing wdt:P17 ?country. }
  { ?Thing wdt:P856 ?official_website. }
  OPTIONAL { ?Thing wdt:P1019 ?web_feed_URL. }
  MINUS { ?Thing wdt:P582 ?end_time. }
  MINUS { ?Thing wdt:P31 wd:Q13442814. }
  OPTIONAL { ?Thing wdt:P9922 ?Flipboard_ID. }
  OPTIONAL { ?Thing wdt:P9852 ?Media_Bias_Fact_Check_ID. }
  OPTIONAL { ?Thing wdt:P10006 ?AllSides_ID. }
  OPTIONAL { ?Thing wdt:P2267 ?PolitiFact_people_and_groups_ID. }
  OPTIONAL { ?Thing wdt:P6157 ?Google_News_publication_ID. }
  OPTIONAL { ?Thing wdt:P2984 ?Snapchat_username. }
  OPTIONAL { ?Thing wdt:P3267 ?Flickr_user_ID. }
  OPTIONAL { ?Thing wdt:P4013 ?Giphy_username. }
  OPTIONAL { ?Thing wdt:P4265 ?Reddit_username. }
  OPTIONAL { ?Thing wdt:P4411 ?Quora_username. }
  OPTIONAL { ?Thing wdt:P856 ?official_website. }
  OPTIONAL { ?Thing wdt:P8904 ?Parler_username. }
  OPTIONAL { ?Thing wdt:P8919 ?Gab_username. }
  OPTIONAL { ?Thing wdt:P2002 ?Twitter_username. }
  OPTIONAL { ?Thing wdt:P2013 ?Facebook_ID. }
  OPTIONAL { ?Thing wdt:P4033 ?Mastodon_address. }
  OPTIONAL { ?Thing wdt:P2397 ?YouTube_channel_ID. }
  OPTIONAL { ?Thing wdt:P7085 ?TikTok_username. }
  OPTIONAL { ?Thing wdt:P3984 ?subreddit. }
  OPTIONAL { ?Thing wdt:P856 ?official_website. }
  OPTIONAL { ?Thing wdt:P6157 ?Google_News_publication_ID. }
  OPTIONAL { ?Thing wdt:P856 ?official_website. }
  OPTIONAL { ?Thing wdt:P3417 ?Quora_topic_ID. }
  OPTIONAL { ?Thing wdt:P2572 ?hashtag. }
  OPTIONAL { ?Thing wdt:P1482 ?Stack_Exchange_tag. }
  OPTIONAL { ?Thing wdt:P8672 ?Twitter_topic_ID. }
  OPTIONAL { ?Thing wdt:P9345 ?Discord_server_numeric_ID. }
  OPTIONAL { ?Thing wdt:P1687 ?Wikidata_property. }
  OPTIONAL { ?Thing wdt:P407 ?language_of_work_or_name. }
  OPTIONAL { ?Thing wdt:P364 ?original_language_of_film_or_TV_show. }
  OPTIONAL { ?Thing wdt:P1142 ?political_ideology. }
  OPTIONAL { ?Thing wdt:P1387 ?political_alignment. }
  MINUS { ?Thing wdt:P576 ?dissolved__abolished_or_demolished_date. }
  MINUS { ?Thing wdt:P582 ?end_time. }
}
"""


class SPRQL:
    def __init__(self, sparql, url) -> None:
        self.sparql = sparql
        self.url = url

    def run(self) -> None:
        da = {}
        # print(self.url)
        while True:
            r = requests.get(self.url, params={
                             'format': 'json', 'query': self.sparql})
            if not r.ok:
                sleep(10)
                print("wilidata eoror")
                print(r)
                continue
            try:
                data = r.json()
            except:
                continue
            break
        for i in data["results"]["bindings"]:
            if i["Thing"]["value"] not in da.keys():
                da[i["Thing"]["value"]] = {}
            for ke in i.keys():
                if not ke in da[i["Thing"]["value"]].keys():
                    da[i["Thing"]["value"]][ke] = []
                if i[ke]["value"] not in da[i["Thing"]["value"]][ke]:
                    da[i["Thing"]["value"]][ke].append(i[ke]["value"])
        return da
