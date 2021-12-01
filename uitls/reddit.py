
from re import sub
import praw
## <YOU DID NOT  SEE THIS>
reddit = praw.Reddit(
    client_id="174uDhuKn6paB-p-KzWqag",
    client_secret="jE4uCAk2x6-ulk8phByKY8zA41ZsCg",
    user_agent="willdor script",
)
## <\YOU DID NOT  SEE THIS>

def reddit_feed(url):
    feeds = []
    for submission in reddit.domain(url).hot(limit=25):
        feeds.append({"title":[(submission.title)],"href":[(submission.url)]})
    return feeds
        

print(reddit_feed("www.bbc.com"))