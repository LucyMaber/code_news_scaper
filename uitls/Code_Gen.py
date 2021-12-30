from bs4 import BeautifulSoup
import requests

from uitls.reqest_man import reqest_saferobot
names = []
dText_ = """
from bs4 import BeautifulSoup
import requests
websites =  {website_string}
countryLabel  = "{countryLabel}"
feed  = {web_feed_URL} 
Flipboard_ID = {Flipboard_ID}
Instagram_username = {Instagram_username}
Media_Bias_Fact_Check_ID = {Media_Bias_Fact_Check_ID}
Gab_username = {Gab_username}
Twitter_username = {Twitter_username}
subreddit = {subreddit}
Google_News_publication_ID = {Google_News_publication_ID}
Flickr_user_ID = {Flickr_user_ID}
Giphy_username = {Giphy_username}
Reddit_username = {Reddit_username}
Quora_username = {Quora_username}
Parler_username = {Parler_username}
Facebook_ID = {Facebook_ID}
Mastodon_address = {Mastodon_address}
YouTube_channel_ID = {YouTube_channel_ID}
TikTok_username = {TikTok_username}
Snapchat_username = {Snapchat_username}
subreddit = {subreddit}
Quora_topic_ID = {Quora_topic_ID}
hashtag = {hashtag}
Stack_Exchange_tag = {Stack_Exchange_tag}
Twitter_topic_ID = {Twitter_topic_ID}
Discord_server_numeric_ID = {Discord_server_numeric_ID}
Wikidata_property = {Wikidata_property}
language_of_work_or_name = {language_of_work_or_name}
political_ideology = {political_ideology}
political_alignment = {political_alignment}
def scan():
{scan}
def article(url):
{article}
def handle(url):
{handle}"""

def scan_for (value,soup,tab, isTime, listP = []):
    found = False
    array = []
    ##
    if len(soup.select('[itemprop="{value}"]'.format(value=value))) != 0:
        found = False
        array.append(("\t"*(tab+0)) + "{value} = soup.select('[itemprop=\"{value}\"]')[0][content].get_text()".format(value=value) )
    elif len(soup.select('time[itemprop="{value}"]'.format(value=value))) != 0:
        found = False
        array.append(("\t"*(tab+0)) + "{value} = soup.select('[itemprop=\"{value}\"]')[0][content].get_text()" .format(value=value))
    elif len(soup.select('meta[itemprop="{value}"]'.format(value=value))) != 0:
        found = False
        array.append(("\t"*(tab+0)) + "{value}=  soup.select('[itemprop=\"{value}\"]')[0][content].get_text()".format(value=value) )
    ##
    elif len(soup.select('[property="{value}"]'.format(value=value))) != 0:
        found = False
        array.append(("\t"*(tab+0)) + "{value} = soup.select('[property=\"{value}\"]')[0][content].get_text()".format(value=value) )
    elif len(soup.select('time[property="{value}"]'.format(value=value))) != 0:
        found = False
        array.append(("\t"*(tab+0)) + "{value} =  soup.select('[property=\"{value}\"]')[0][content].get_text()" .format(value=value))
    elif len(soup.select('meta[property="{value}"]'.format(value=value))) != 0:
        found = False
        array.append(("\t"*(tab+0)) + "i = soup.select('[property=\"{value}\"]')[0][content].get_text()".format(value=value) )
    elif len(soup.select('.{value}'.format(value=value))) != 0:
        found = False
        array.append(("\t"*(tab+0)) + "{value} = soup.select('.{value}').get_text()".format(value=value) )
    return array ,found


class CodeGen:
    def __init__(self, url=[], feed=[]) -> None:
        self.url =url +feed
        

    def gen_handle(self):
        pass

    def gen_article_time(self,soup,tab):
        if len(soup.select('.datePublished > time')) != 0 and len(soup.select('.dateModified > time' )) != 0:
            pass

    def gen_article_articleBody	(self,soup,tab):
        #string
        array ,found = scan_for ("articleBody",soup,tab, True, listP = [])
        if not found :
            array ,found = scan_for ("text",soup,tab, True, listP = [])
        if found:
            return array
        elif len(soup.select('[class="has-content-area"]')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('[class=\"has-content-area\"]')[0].get_text()"]
        elif len(soup.select('[class="has-content-area"]')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('[class=\"vy-cx-page-content \"]')[0].get_text() "]
        elif len(soup.select('[data-test="article-body-text"]')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('[data-test=\"vy-cx-page-content \"]')[0].get_text()"]
        elif len(soup.select('.p402_hide > div')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.p402_hide > div')[0].get_text()"]
        elif len(soup.select('#content-wrapper')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('#content-wrapper')[0].get_text()"]
        elif len(soup.select('.entry-content')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.entry-content')[0].get_text()"]
        elif len(soup.select('.post-content')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.post-content')[0].get_text()"]
        elif len(soup.select('[data-type="article-body"]')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('[data-type=\"article-body\"]')[0].get_text()"]
        elif len(soup.select('#article_content')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('#article_content')[0].get_text()"]
        elif len(soup.select('.text')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.text')[0].get_text()"]
        elif len(soup.select('#single-article-content')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('#single-article-content')[0].get_text()"]
        elif len(soup.select('#content-wrapper')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('#content-wrapper')[0].get_text()"]
        elif len(soup.select('#subscription-content')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('#subscription-content')[0].get_text()"]
        elif len(soup.select('[class="entry clearfix"]')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('[class=\"entry clearfix\"]')[0].get_text()"]
        elif len(soup.select('.p402_hide')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.p402_hide')[0].get_text() "]
        elif len(soup.select('.article-content')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.article-content')[0].get_text()"]
        elif len(soup.select('.entry-content')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.entry-content')[0].get_text()"]
        elif len(soup.select('.detay-icerik')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.detay-icerik')[0].get_text()"]
        elif len(soup.select('.Article__content > div')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.Article__content > div')[0].get_text()"]
        elif len(soup.select('.entry-content')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.entry-content')[0].get_text()"]
        elif len(soup.select('.article_bodycopy')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.article_bodycopy')[0].get_text()"]
        elif len(soup.select('#article-body')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('#article-body')[0].get_text()"]
        elif len(soup.select('#post-content')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('#post-content')[0].get_text()"]
        elif len(soup.select('.td-post-content')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.td-post-content')[0].get_text()"]
        elif len(soup.select('.pagestory')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.pagestory')[0].get_text()"]
        elif len(soup.select('.bigtext')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.bigtext')[0].get_text()"]
        elif len(soup.select('[itemprop="text"] > div')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('[itemprop=\'text\'] > div')[0].get_text()"]
        elif len(soup.select('.article__detail-text')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.content')[0].get_text()"]
        elif len(soup.select('.article__detail-text')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.article__detail-text')[0].get_text()"]
        elif len(soup.select('.entry')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.entry')[0] "]
        elif len(soup.select(".article-text")) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.article-text')[0].get_text()"]
        elif len(soup.select('div.ms-article-content') ) != 0:
            return [("\t"* tab) +"articleBody = soup.select('div.ms-article-content')[0].get_text() "]
        elif len(soup.select('.t-content__body') ) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.t-content__body')[0].get_text()"]
        elif len(soup.select('.body__inner-container')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.body__inner-container')[0].get_text() "]
        elif len(soup.select('#story-body-container')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('#story-body-container')[0].get_text()"]
        elif len(soup.select('.entry')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.entry')[0].get_text() "]
        elif len(soup.select('.newsfull__body') ) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.newsfull__body')[0].get_text() "]
        elif len(soup.select('#main')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('#main')[0].get_text()"]
        elif len(soup.select('[class="has-content-area"]')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('[class=\"has-content-area\"]')[0].get_text()"]
        elif len(soup.select('[class="RichTextArticleBody-body RichTextBody"]')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('[class=\"RichTextArticleBody-body RichTextBody\"]')[0].get_text()"]
        elif len(soup.select('[class="c-article__content e-content"]')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('[class=\"c-article__content e-content\"]')[0].get_text()"]
        elif len(soup.select('.body')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.body')[0].get_text()"]
        elif len(soup.select('.c-article__content')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.c-article__content')[0.get_text()] "]
        elif len(soup.select('.secondcontent')) != 0:
            return [("\t"* tab) +"articleBody = soup.select(.secondcontent')[0].get_text() "]
        elif len(soup.select('.c-article__content')) != 0:
            return [("\t"* tab) +"articleBody = soup.select('.c-article__content')[0].get_text() "]
        elif len(soup.select('article') ) != 0:
            return [("\t"* tab) +"articleBody = soup.select('article')[0].get_text()"]
    def gen_article_articleSection	(self,soup,tab):
        #string
        array ,found = scan_for ("articleSection",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_backstory(self,soup,tab):
        #string
        array ,found = scan_for ("backstory",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_assesses(self,soup,tab):
        #string
        array ,found = scan_for ("assesses",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_award(self,soup,tab):
        #string
        array ,found = scan_for ("award",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_awards(self,soup,tab):
        #string
        array ,found = scan_for ("awards",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_conditionsOfAccess(self,soup,tab):
        #string
        array ,found = scan_for ("conditionsOfAccess",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_contentRating(self,soup,tab):
        array ,found = scan_for ("contentRating",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_creditText(self,soup,tab):
        #string
        array ,found = scan_for ("creditText",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_dateCreated(self,soup,tab):
        #time
        array ,found = scan_for ("dateCreated",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_dateModified(self,soup,tab):
        #time
        array ,found = scan_for ("dateModified",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_datePublished(self,soup,tab):
        #time
        array ,found = scan_for ("datePublished",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_pattern(self,soup,tab):
        #string
        array ,found = scan_for ("pattern",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_text(self,soup,tab):
        #string
        array ,found = scan_for ("text",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_typicalAgeRange(self,soup,tab):
        #string
        array ,found = scan_for ("string",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_version(self,soup,tab):
        #string
        array ,found = scan_for ("version",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_alternateName(self,soup,tab):
        #string
        array ,found = scan_for ("alternateName",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_description(self,soup,tab):
        array ,found = scan_for ("description",soup,tab, True, listP = [])
        if found:
            return array
        elif len(soup.select('#content-wrapper > h2')) != 0:
            array.append(("\t"*tab)+"description = soup.select('#content-wrapper > h2')[0].get_text()")
        elif len(soup.select('.metabox > h4')) != 0:
            array.append(("\t"*tab)+"description = soup.select('.metabox > h4')[0].get_text()")
        elif len(soup.select('.body-excerpt > p')) != 0:
            array.append(("\t"*tab)+"description = soup.select('.body-excerpt > p')[0].get_text()")
        elif len(soup.select('h2.polaris__heading')) != 0:
            array.append(("\t"*tab)+"description = soup.select('h2.polaris__heading')[0].get_text()")
        elif len(soup.select('h2.c-header__intro ')) != 0:
            array.append(("\t"*tab)+"description = soup.select('h2.c-header__intro ')[0].get_text()")
        elif len(soup.select('.post-full-custom-excerpt')) != 0:
            array.append(("\t"*tab)+"description = soup.select('.post-full-custom-excerpt')[0].get_text()")
        elif len(soup.select('div > div > div.col-8.single-maincol > p.intropara')) != 0:
            array.append(("\t"*tab)+"description = soup.select('div > div > div.col-8.single-maincol > p.intropara')[0].get_text()")
        elif len(soup.select('#content-wrapper > h2')) != 0:
            array.append(("\t"*tab)+"description = soup.select('#content-wrapper > h2')[0].get_text()")
        elif len(soup.select('.td-post-content')) != 0:
            array.append(("\t"*tab)+"description = soup.select('.td-post-content')[0].get_text()")
        elif len(soup.select('.newspack-post-subtitle')) != 0:
            array.append(("\t"*tab)+"description = soup.select('.newspack-post-subtitle'))[0[0].get_text()")
        elif len(soup.select('.quote')) != 0:
            array.append(("\t"*tab)+"description = soup.select('.quote')[0].get_text()")
        elif len(soup.select('header.details-header > h4')) != 0:
            array.append(("\t"*tab)+"description = soup.select('header.details-header > h4')[0].get_text()")
        elif len(soup.select('.c-article-excerpt')) != 0:
            array.append(("\t"*tab)+"description = soup.select('.c-article-excerpt')[0].get_text()")
        elif len(soup.select('.sdc-article-header__sub-title')) != 0:
            array.append(("\t"*tab)+"description = soup.select('.sdc-article-header__sub-title')[0].get_text()")
        elif len(soup.select('#main > div > h2')) != 0:
            array.append(("\t"*tab)+"description = soup.select('#main > div > h2')[0].get_text()")
        elif len(soup.select('p.hdr-description')) != 0:
            array.append(("\t"*tab)+"description = soup.select('p.hdr-description')[0].get_text()")
        elif len(soup.select('.header > hgroup > h2')) != 0:
            array.append(("\t"*tab)+"description = soup.select('.header > hgroup > h2')[0].get_text()")
        elif len(soup.select('.strapline')) != 0:
            array.append(("\t"*tab)+"description = soup.select('.strapline')[0].get_text()")
        else:
            return []
    def gen_article_name(self,soup,tab):
        array ,found = scan_for ("name",soup,tab, True, listP = [])
        if found:
            return array
        return []
    def gen_article_dateline(self,soup,tab):
        array ,found = scan_for ("dateline",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_abstract(self,soup,tab):
        array ,found = scan_for ("abstract",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_correction(self,soup,tab):
        array ,found = scan_for ("correction",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_comment(self,soup,tab):
        array ,found = scan_for ("comment",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_inLanguage(self,soup,tab):
        array ,found = scan_for ("inLanguage",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_headline(self,soup,tab):
        array ,found = scan_for ("headline",soup,tab, True, listP = [])
        if found:
            return array
        elif len(soup.select('.headline')) != 0:
            return [("\t"* tab) +"headline = soup.select('.headline')[0].get_text()"]
        elif len(soup.select('.page-title > div')) != 0:
            return [("\t"*tab)+ "soup.select('.page-title > div')"]
        elif len(soup.select(' div > div > div.col-8.single-maincol > h1')) != 0:
            return [("\t"*tab)+ "soup.select(' div > div > div.col-8.single-maincol > h1')"]
        elif len(soup.select('.article__headline')) != 0:
            return [("\t"*tab)+ "soup.select('.article__headline')"]
        elif len(soup.select('.Article__main > div > div > div > h1')) != 0:
            return [("\t"*tab)+ "soup.select('.Article__main > div > div > div > h1')"]
        elif len(soup.select('.article__title')) != 0:
            return [("\t"*tab)+ "soup.select('.article__title')"]
        elif len(soup.select('.article-details > h1')) != 0:
            return [("\t"*tab)+ "soup.select('.article-details > h1')"]
        elif len(soup.select('.article-header-inner > h1')) != 0:
            return [("\t"*tab)+ "soup.select('.article-header-inner > h1')"]
        elif len(soup.select('.articleHeader > h1')) != 0:
            return [("\t"*tab)+ "soup.select('.articleHeader > h1')"]
        elif len(soup.select('.biggerheading')) != 0:
            return [("\t"*tab)+ "soup.select('.biggerheading')"]
        elif len(soup.select('.blog-post-title-font')) != 0:
            return [("\t"*tab)+ "soup.select('.blog-post-title-font')"]
        elif len(soup.select('.c-article-header__title')) != 0:
            return [("\t"*tab)+ "soup.select('.c-article-header__title')"]
        elif len(soup.select('.caption-text > h1')) != 0:
            return [("\t"*tab)+ "soup.select('.caption-text > h1')"]
        elif len(soup.select('.entry-header > h1')) != 0:
            return [("\t"*tab)+ "soup.select('.entry-header > h1')"]
        elif len(soup.select('.entry-title')) != 0:
            return [("\t"*tab)+ "soup.select('.entry-title')"]
        elif len(soup.select('.header > hgroup > h1')) != 0:
            return [("\t"*tab)+ "soup.select('.header > hgroup > h1')"]
        elif len(soup.select('.headline ')) != 0:
            return [("\t"*tab)+ "soup.select('.headline ')"]
        elif len(soup.select('.headline-with-subtype > h1')) != 0:
            return [("\t"*tab)+ "soup.select('.headline-with-subtype > h1')"]
        elif len(soup.select('.main-content > div > h1')) != 0:
            return [("\t"*tab)+ "soup.select('.main-content > div > h1')"]
        elif len(soup.select('.main-title')) != 0:
            return [("\t"*tab)+ "soup.select('.main-title')"]
        elif len(soup.select('.np-single_title')) != 0:
            return [("\t"*tab)+ "soup.select('.np-single_title')"]
        elif len(soup.select('.o-headline')) != 0:
            return [("\t"*tab)+ "soup.select('.o-headline')"]
        elif len(soup.select('.post-full-title')) != 0:
            return [("\t"*tab)+ "soup.select('.post-full-title')"]
        elif len(soup.select('.post-title ')) != 0:
            return [("\t"*tab)+ "soup.select('.post-title ')"]
        elif len(soup.select('.sdc-site-component-header--h1')) != 0:
            return [("\t"*tab)+ "soup.select('.sdc-site-component-header--h1')"]
        elif len(soup.select('.section_content > h2')) != 0:
            return [("\t"*tab)+ "soup.select('.section_content > h2')"]
        elif len(soup.select('.story__headline')) != 0:
            return [("\t"*tab)+ "soup.select('.story__headline')"]
        elif len(soup.select('.story-headline')) != 0:
            return [("\t"*tab)+ "soup.select('.story-headline')"]
        elif len(soup.select('.title-section > h1')) != 0:
            return [("\t"*tab)+ "soup.select('.title-section > h1')"]
        elif len(soup.select('.title')) != 0:
            return [("\t"*tab)+ "soup.select('.title')"]
        elif len(soup.select('.uk-article-title')) != 0:
            return [("\t"*tab)+ "soup.select('.uk-article-title')"]
        elif len(soup.select('[class="article__title mdc-typography--headline4"]')) != 0:
            return [("\t"*tab)+ "soup.select('[class=\"article__title mdc-typography--headline4\"]')"]
        elif len(soup.select('[class="fl-heading-text"]')) != 0:
            return [("\t"*tab)+ "soup.select('[class=\"fl-heading-text\"]')"]
        elif len(soup.select('[class="ne-article__title"] ')) != 0:
            return [("\t"*tab)+ "soup.select('[class=\"ne-article__title\"] ')"]
        elif len(soup.select('[itemprop="headline name"]')) != 0:
            return [("\t"*tab)+ "soup.select('[itemprop=\"headline name\"]')"]
        elif len(soup.select('[itemprop="name"]') ) != 0:
            return [("\t"*tab)+ "soup.select('[itemprop=\"name\"]') "]
        elif len(soup.select('#article > h1')) != 0:
            return [("\t"*tab)+ "soup.select('#article > h1')"]
        elif len(soup.select('#article > h1')) != 0:
            return [("\t"*tab)+ "soup.select('#article > h1')"]
        elif len(soup.select('#ColLeft > h1')) != 0:
            return [("\t"*tab)+ "soup.select('#ColLeft > h1')"]
        elif len(soup.select('#content-wrapper > h1')) != 0:
            return [("\t"*tab)+ "soup.select('#content-wrapper > h1')"]
        elif len(soup.select('#content-wrapper > h1')) != 0:
            return [("\t"*tab)+ "soup.select('#content-wrapper > h1')"]
        elif len(soup.select('#main > .entry > #topslug > a')) != 0:
            return [("\t"*tab)+ "soup.select('#main > .entry > #topslug > a')"]
        elif len(soup.select('#main-heading') ) != 0:
            return [("\t"*tab)+ "soup.select('#main-heading') "]
        elif len(soup.select('#single-article-title')) != 0:
            return [("\t"*tab)+ "soup.select('#single-article-title')"]
        elif len(soup.select('header > .title')) != 0:
            return [("\t"*tab)+ "soup.select('header > .title')"]
        elif len(soup.select('header > h1')) != 0:
            return [("\t"*tab)+ "soup.select('header > h1')"]
        elif len(soup.select('header.details-header > h2')) != 0:
            return [("\t"*tab)+ "soup.select('header.details-header > h2')"]
        elif len(soup.select(".story-headline")) != 0:
            return [("\t"*tab)+ "soup.select(\".story-headline\")"]
        elif len(soup.select("#content-wrapper > h1 ")) != 0:
            return [("\t"*tab)+ "soup.select(\"#content-wrapper > h1\")"]
        elif len(soup.select('div.headline-with-subtype') ) != 0:
            return [("\t"*tab)+ "soup.select('div.headline-with-subtype') "]
        elif len(soup.select('.left > h1')) != 0:
            return [("\t"*tab)+ "soup.select('.left > h1')"]
        elif len(soup.select('article > div > div > div > div > div > h1')) != 0:
            return [("\t"*tab)+ "soup.select('article > div > div > div > div > div > h1')"]
        elif len(soup.select('article > div.story-topper.lede.column.eleven-column > h1')) != 0:
            return [("\t"*tab)+ "soup.select('article > div.story-topper.lede.column.eleven-column > h1')"]
        elif len(soup.select('article > h1')) != 0:
            return [("\t"*tab)+ "soup.select('article > h1')"]
        elif len(soup.select('div > h1')) != 0:
            return [("\t"*tab)+ "soup.select('div > h1')"]
        elif len(soup.select('h1.article__title ')) != 0:
            return [("\t"*tab)+ "soup.select('h1.article__title ')"]
        elif len(soup.select('h1.article-headline')) != 0:
            return [("\t"*tab)+ "soup.select('h1.article-headline')"]
        elif len(soup.select('h1.c-header__heading ')) != 0:
            return [("\t"*tab)+ "soup.select('h1.c-header__heading ')"]
        elif len(soup.select('h1.chapter-ttl')) != 0:
            return [("\t"*tab)+ "soup.select('h1.chapter-ttl')"]
        elif len(soup.select('h1.entry-title ')) != 0:
            return [("\t"*tab)+ "soup.select('h1.entry-title ')"]
        elif len(soup.select('h1.headline ') ) != 0:
            return [("\t"*tab)+ "soup.select('h1.headline ') "]
        elif len(soup.select('h1.intro-side-heading ')) != 0:
            return [("\t"*tab)+ "soup.select('h1.intro-side-heading ')"]
        elif len(soup.select('h1.opinion-title')) != 0:
            return [("\t"*tab)+ "soup.select('h1.opinion-title')"]
        elif len(soup.select('h1.po-hr-cn__title ')) != 0:
            return [("\t"*tab)+ "soup.select('h1.po-hr-cn__title ')"]
        elif len(soup.select('h1.polaris__heading')) != 0:
            return [("\t"*tab)+ "soup.select('h1.polaris__heading')"]
        elif len(soup.select('h1.post_title')) != 0:
            return [("\t"*tab)+ "soup.select('h1.post_title')"]
        elif len(soup.select('h1.tdb-title-text')) != 0:
            return [("\t"*tab)+ "soup.select('h1.tdb-title-text')"]
        elif len(soup.select('h1.title')) != 0:
            return [("\t"*tab)+ "soup.select('h1.title')"]
        elif len(soup.select('h1')) != 0:
            return [("\t"*tab)+ "soup.select('h1')"]
        elif len(soup.select('h1[class="entry-title"]')) != 0:
            return [("\t"*tab)+ "soup.select('h1[class=\"entry-title\"]')"]
        else:
            return []
    def gen_article_expires(self,soup,tab):
        array ,found = scan_for ("expires",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_genre(self,soup,tab):
        array ,found = scan_for ("genre",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_isAccessibleForFree(self,soup,tab):
        array ,found = scan_for ("isAccessibleForFree",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_isBasedOn(self,soup,tab):
        array ,found = scan_for ("isBasedOf",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_isFamilyFriendly(self,soup,tab):
        array ,found = scan_for ("isFamilyFriendly",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_sdDatePublished(self,soup,tab):
        array ,found = scan_for ("sdDatePublished",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_version(self,soup,tab):
        array ,found = scan_for ("version",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_reviewBody(self,soup,tab):
        array ,found = scan_for ("reviewBody",soup,tab, True, listP = [])
        if not found :
            array ,found = scan_for ("text",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_reviewAspect(self,soup,tab):
        array ,found = scan_for ("reviewAspect",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_reviewRating(self,soup,tab):
        array ,found = scan_for ("reviewRating",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_positiveNotes(self,soup,tab):
        array ,found = scan_for ("positiveNote",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_negativeNotes(self,soup,tab):
        array ,found = scan_for ("negativeNotes",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_itemReviewed(self,soup,tab):
        array ,found = scan_for ("itemReviewed",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_associatedReview(self,soup,tab):
        array ,found = scan_for ("associatedReview",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_associatedMediaReview(self,soup,tab):
        array ,found = scan_for ("associatedMediaReview",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []
    def gen_article_associatedClaimReview(self,soup,tab):
        array ,found = scan_for ("associatedClaimReview",soup,tab, True, listP = [])
        if found:
            return array
        else:
            return []

    def gen_article_article(self,urls):
        seen = []
        code = []
        for url in urls:
            print("GEN:",url)
            array = []
            r = reqest_saferobot(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            array = array + [(("\t"*1)+"try:")]
            array = array + (self.gen_article_articleBody(soup,2))
            array = array + (self.gen_article_articleSection(soup,2))
            array = array + (self.gen_article_backstory(soup,2))
            array = array + (self.gen_article_assesses(soup,2))
            array = array + (self.gen_article_award(soup,2))
            array = array + (self.gen_article_awards(soup,2))
            array = array + (self.gen_article_conditionsOfAccess(soup,2))
            array = array + (self.gen_article_contentRating(soup,2))
            array = array + (self.gen_article_dateCreated(soup,2))
            array = array + (self.gen_article_dateModified(soup,2))
            array = array + (self.gen_article_datePublished(soup,2))
            array = array + (self.gen_article_pattern(soup,2))
            array = array + (self.gen_article_text(soup,2))
            array = array + (self.gen_article_typicalAgeRange(soup,2))
            array = array + (self.gen_article_version(soup,2))
            array = array + (self.gen_article_alternateName(soup,2))
            array = array + (self.gen_article_description(soup,2))
            array = array + (self.gen_article_name(soup,2))
            array = array + (self.gen_article_dateline(soup,2))
            array = array + (self.gen_article_abstract(soup,2))
            array = array + (self.gen_article_correction(soup,2))
            array = array + (self.gen_article_comment(soup,2))
            array = array + (self.gen_article_inLanguage(soup,2))
            array = array + (self.gen_article_headline(soup,2))
            array = array + (self.gen_article_expires(soup,2))
            array = array + (self.gen_article_genre(soup,2))
            array = array + (self.gen_article_isAccessibleForFree(soup,2))
            array = array + (self.gen_article_isBasedOn(soup,2))
            array = array + (self.gen_article_isFamilyFriendly(soup,2))
            array = array + (self.gen_article_sdDatePublished(soup,2))
            array = array + [(("\t"*1)+"except:")]
            array.append(("\t"*2)+"articleBody = None")
            array.append(("\t"*2)+"articleSection = None")
            array.append(("\t"*2)+"backstory = None")
            array.append(("\t"*2)+"assesses = None")
            array.append(("\t"*2)+"award = None")
            array.append(("\t"*2)+"awards = None")
            array.append(("\t"*2)+"conditionsOfAccess = None")
            array.append(("\t"*2)+"contentRating = None")
            array.append(("\t"*2)+"dateCreated = None")
            array.append(("\t"*2)+"dateModified = None")
            array.append(("\t"*2)+"datePublished = None")
            array.append(("\t"*2)+"pattern = None")
            array.append(("\t"*2)+"text = None")
            array.append(("\t"*2)+"typicalAgeRange = None")
            array.append(("\t"*2)+"version = None")
            array.append(("\t"*2)+"alternateName = None")
            array.append(("\t"*2)+"description = None")
            array.append(("\t"*2)+"name = None")
            array.append(("\t"*2)+"articleSection = None")
            array.append(("\t"*2)+"dateline = None")
            array.append(("\t"*2)+"abstract = None")
            array.append(("\t"*2)+"correction = None")
            array.append(("\t"*2)+"comment = None")
            array.append(("\t"*2)+"inLanguage = None")
            array.append(("\t"*2)+"headline = None")
            array.append(("\t"*2)+"expires = None")
            array.append(("\t"*2)+"genre = None")
            array.append(("\t"*2)+"isAccessibleForFree = None")
            array.append(("\t"*2)+"isBasedOn = None")
            array.append(("\t"*2)+"isFamilyFriendly = None")
            array.append(("\t"*2)+"sdDatePublished = None")
            code = code + array 
            output ="\n".join(array)
            if output in seen:
                continue
            seen.append(output)

    def gen_scan(self):
        pass

    def gen(self):
        dText = dText_.format(
            website_string="[]",
            handle="\n   return False",
            article=self.gen_article()
            )

