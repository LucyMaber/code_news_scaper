def getPost(id):
    url = "https://hacker-news.firebaseio.com/v0/item/{id}".format(id =id)

def getStories():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"