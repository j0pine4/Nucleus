import pandas as pd
from pytrends.request import TrendReq
import pytrends
import json
import pprint
import requests
import time
import os

risingQueriesVAR = []
topQueriesVAR = []

def risingTopics(input):
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=[input])

    relatedTopics = pytrends.related_topics()

    dg = relatedTopics.get(input).get('rising')
    dictionary = {'Title' : dg['topic_title'],'Topic Type' : dg['topic_type']}
    df = pd.DataFrame(dictionary)
    df.to_csv('CSV Files/Rising_Topics.csv')

def topTopics(input):
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=[input])

    relatedTopics = pytrends.related_topics()

    dg = relatedTopics.get(input).get('top')
    dictionary = {'Title' : dg['topic_title'],'Topic Type' : dg['topic_type']}
    df = pd.DataFrame(dictionary)
    df.to_csv('CSV Files/Top_Topics.csv')

def risingQueries(input):

    pytrends = TrendReq()

    pytrends.build_payload(kw_list=[input], geo='US')


    related_queries = pytrends.related_queries()

    dg = related_queries.get(input).get('rising')

    df = pd.DataFrame(dg)
    df.to_csv('CSV Files/RisingKeywords.csv')

    for item in dg['query']:
        risingQueriesVAR.append(item)


def topQueries(input):

    pytrends = TrendReq()

    pytrends.build_payload(kw_list=[input], geo='US')


    related_queries = pytrends.related_queries()

    dg = related_queries.get(input).get('top')

    df = pd.DataFrame(dg)
    df.to_csv('CSV Files/topKeywords.csv')

    for item in dg['query']:
        topQueriesVAR.append(item)

def trendingTopics(inputList, csvName):
    pytrends = TrendReq()
    searches = inputList


    groupkeywords = list(zip(*[iter(searches)] * 1))
    groupkeywords = [list(x) for x in groupkeywords]

    dicti = {}
    i = 1
    for trending in groupkeywords:
        pytrends.build_payload(trending, timeframe='today 3-m', geo='GB')
        dicti[i] = pytrends.interest_over_time()
        i += 1

    result = pd.concat(dicti, axis=1)
    result.columns = result.columns.droplevel(0)
    result = result.drop('isPartial', axis=1)

    result.reset_index(level=0, inplace=True)
    result = pd.melt(result, id_vars='date', value_vars=searches)

    result.to_csv(csvName)

def cityData(input):
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=[input], geo='US')

    dg = pytrends.interest_by_region(resolution='CITY', inc_low_vol=True, inc_geo_code=False)
    df = pd.DataFrame(dg)
    df.rename(columns= {input : 'Value'}, inplace=True)
    df.to_csv('CSV Files/cityData.csv')


def metroData(input):
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=[input], geo='US')

    dg = pytrends.interest_by_region(resolution='DMA', inc_low_vol=True, inc_geo_code=False)
    df = pd.DataFrame(dg)
    df.rename(columns= {input : 'Value'}, inplace=True)
    df.to_csv('CSV Files/metroData.csv')

def regionData(input):
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=[input], geo='US')

    dg = pytrends.interest_by_region(resolution='REGION', inc_low_vol=True, inc_geo_code=False)
    df = pd.DataFrame(dg)
    df.rename(columns= {input : 'Value'}, inplace=True)
    df.to_csv('CSV Files/regionData.csv')

def currentTrends():
    pytrends = TrendReq()

    trends = pytrends.trending_searches(pn='united_states')

    trends.to_csv('CSV Files/currentTrends.csv')








