import tweepy
import pprint
import json
import pandas as pd


def twitter_data(input):
    #Variables that contain user credentials
    ACCESS_TOKEN = '161866664-iuPHrfjwJyd3g7ggWRFopKKQQvyPmVBP01s8c5GA'
    ACCESS_TOKEN_SECRET = 'BYlDj5QhYJkynmzDL79XWOpZaLYX5aqbkUiJWjDHvM02i'
    CONSUMER_KEY = 'eTTpPK7D4slLDvPzJakzQQ6zE'
    CONSUMER_SECRET = '2oSLbj3KDXiptyRmbHkMyWtcDGbyy0eSnFL6gQTVn58EGbVgED'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


    api = tweepy.API(auth)
    url_rest = "https://api.twitter.com/1.1/search/tweets.json"
    hashtag_input = '#' + input
    max_tweets = 100

    trending_search = api.trends_place(23424977)

    trending_hashtags = []
    hashtag_search = []

    trends = trending_search[0]['trends']

    for trend in trends:
        name = trend['name']
        if name.startswith('#'):
            trending_hashtags.append(name)

    # print(trending_hashtags)

    for tweet in tweepy.Cursor(api.search, q=hashtag_input, rpp=100).items(max_tweets):
        for item in [tweet.text]:
            if item.startswith('#'):
                hash = item.split('#')
                hashtag_search.append(hash)


    print(hashtag_search)

    df = pd.DataFrame(trending_hashtags)
    df.to_csv('CSV Files/Trending_Hashtags.csv')

    df = pd.DataFrame(hashtag_search)
    df.to_csv('CSV Files/Hashtag_Search.csv')

twitter_data('halo')








