import tweepy
from elasticsearch import helpers
from tweet_model import map_tweet_for_es
from backends import get_backend
import credentials
import settings

# unicode mgmt
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# go get elasticsearch connection
backend = get_backend.Backend()
datastore = backend.setup()

# auth & api handlers
auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# load topics & build a search
topics = ["oath keeper"]
search = api.search(q=topics, count=100)


# function for screen_name, text, search topic
def tweet_text():
    for tweet in search:
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
            yield map_tweet_for_es(tweet, topics)


# TODO clean up
if backend.backend == 'ES':
    # bulk insert into twitter index
    helpers.bulk(datastore, tweet_text(), index='twitter', doc_type='tweets')
    messages = datastore.search(index="twitter", size=1000, _source=['message'])
    print(messages)

elif backend.backend == 'SQLITE':
    for tweet in search:
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
            tweet_dict = map_tweet_for_es(tweet, topics)
            tweet_dict['topics'] = str(tweet_dict['topics'])

            # TODO create save function
            table = datastore[settings.TABLE_NAME]
            table.insert(tweet_dict)






# view the message field in the twitter index
