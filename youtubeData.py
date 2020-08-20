from googleapiclient.discovery import build
import json
import re
import pprint
import pandas as pd
from pytrends.request import TrendReq
import pytrends


yt_risingQueriesVAR = []
yt_topQueriesVAR = []


def youtube_api(input):
    api_key = 'AIzaSyCZrRnFzZxJ3szNYvLVHLoUq1qbdMLVk40'
    youtubeVideoLink = 'https://www.youtube.com/watch?v='
    youtubeChannelLink = 'https://www.youtube.com/channel/'
    youtubePlaylistLink = 'https://www.youtube.com/results?search_query='
    channelList  = []
    titleList = []
    thumbnailList = []
    itemList = []
    linkList = []

    APIdata = {'Channel Name:' : [], 'Title:' : [], 'Thumbnail:' : [], 'Link:' : [] }


    youtube = build(serviceName='youtube', version='v3', developerKey=api_key)

    request = youtube.search().list(
        part = 'snippet',
        q = input,
        maxResults = 50
        )

    response = request.execute()

    for item in response['items']:
        channelList.append(item['snippet']['channelTitle'])
        titleList.append(item['snippet']['title'])
        thumbnailList.append(item['snippet']['thumbnails']['high']['url'])
        if item['id']['kind'] == 'youtube#video':
            linkList.append(youtubeVideoLink + item['id']['videoId'])
        elif item['id']['kind'] == 'youtube#playlist':
            linkList.append(youtubePlaylistLink + item['id']['playlistId'])
        else:
            linkList.append(youtubeChannelLink + item['id']['channelId'])


    for item in channelList:
        APIdata['Channel Name:'].append(item)

    for item in titleList:
        APIdata['Title:'].append(item)

    for item in thumbnailList:
        APIdata['Thumbnail:'].append(item)

    for item in linkList:
        APIdata['Link:'].append(item)

    data = APIdata

    df = pd.DataFrame.from_dict(data)
    df.to_csv('CSV Files/youtubeData.csv')


def yt_risingQueries(input):

    pytrends = TrendReq()

    pytrends.build_payload(kw_list=[input], geo='US', gprop='youtube')


    related_queries = pytrends.related_queries()

    dg = related_queries.get(input).get('rising')

    df = pd.DataFrame(dg)
    df.to_csv('CSV Files/youtube_RisingKeywords.csv')

    for item in dg['query']:
        yt_risingQueriesVAR.append(item)



def yt_topQueries(input):

    pytrends = TrendReq()

    pytrends.build_payload(kw_list=[input], geo='US', gprop='youtube')


    related_queries = pytrends.related_queries()

    dg = related_queries.get(input).get('top')

    df = pd.DataFrame(dg)
    df.to_csv('CSV Files/youtube_topKeywords.csv')

    for item in dg['query']:
        yt_topQueriesVAR.append(item)

