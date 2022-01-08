
import asyncio
from re import sub
from urllib.parse import urlparse
import enlighten
import asyncpraw
import settings
# <YOU DID NOT  SEE THIS>


# reddit = asyncpraw.Reddit(
#     client_id=settings.reddit_client_id,
#     client_secret=settings.reddit_client_secret,
#     user_agent=settings.reddit_user_agent,
#     check_for_async=False
# )
# <\YOU DID NOT  SEE THIS>


async def reddit_feed_hot_domain(url, reddit, limit=None):
    feeds = []
    domain = urlparse(url)
    if domain.netloc == "":
        domain = url
    else:
        domain = domain.netloc
    print(domain)
    for submission in reddit.domain(domain).hot(limit=None):
        feeds.append(redditProsses(submission))
    feeds = await asyncio.gather(*feeds)
    return feeds




async def reddit_feed_top_domain(url, reddit, top="all", limit=None):
    domain = urlparse(url)
    try:
        feeds = []
        f = reddit.domain(domain.netloc)
        async for submission in f.top(top):
            feeds.append(redditProsses(submission))
    except Exception as e:
        print(e)
    return feeds


async def reddit_feed_new(url, reddit, limit=None):
    domain = urlparse(url).netloc
    feeds = []
    try:
        for submission in  reddit.domain(domain).new(limit=limit):
            feeds.append(redditProsses(submission))
    except:
        print("reddit_error:", domain)
    return feeds


def redditProsses(submission):
    print(submission.url)
    r = {
        "title": submission.title,
        "url": submission.url,
        "upvote_ratio": submission.upvote_ratio,
        "spoiler": submission.spoiler,
        "score": submission.score,
        "over_18": submission.over_18,
        "name": submission.name,
        "locked": submission.locked,
        "subreddit.display_name": submission.subreddit.display_name,
        #"subreddit.id": submission.subreddit.id,
        #"subreddit.name": submission.subreddit.name,
        #"subreddit.over18": submission.subreddit.over18,
    }
    try:
        r["author.created_utc"] = submission.author
    except:
        pass
    try:
        r["author.created_utc"] = submission.author.created_utc
    except:
        pass
    try:
        r["author.has_verified_email"] = submission.author.has_verified_email
    except:
        pass
    try:
        r["author.id"] = submission.author.id
    except:
        pass
    try:
        r["author.is_employee"] = submission.author.is_employee
    except:
        pass
    try:
        r["author.is_mod"] = submission.author.is_mod
    except:
        pass
    try:
        r["author.is_gold"] = submission.author.is_gold
    except:
        pass
    try:
        r["author.name"] = submission.author.name
    except:
        pass
    try:
        r["author.is_suspended"] = submission.author.is_suspended
    except:
        pass
    try:
        r["author.link_karma"] = submission.author.link_karma
    except:
        pass
    return r


if __name__ == "__main__":
    a = reddit_feed_hot_domain("http://www.bbc.com")
    print(a)
