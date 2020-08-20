import sys
#from PyQt5 import QtWidgets
from wordsAPI import wordsAPI, wordsList
from googleSheets import sheetsUpload
from googleData import risingQueries, topQueries, risingQueriesVAR, topQueriesVAR
from googleData import risingTopics, topTopics, cityData, regionData, metroData, trendingTopics, currentTrends
from youtubeData import yt_risingQueries, yt_topQueries, youtube_api
from youtubeData import yt_topQueriesVAR, yt_risingQueriesVAR
from fileManager import fileManager, FILE_LIST
from twitterData import twitter_data
import time

keyword = 'art'
suggestions = [keyword]

# Turn this user input into a usable variable calls userText
userText = keyword
print('Looking for Relevant information for %s' % (userText))


# Run the words API on user input
print('Finding words Associatied to %s' % userText)
wordsAPI(userText)
trendingTopics(wordsList, 'CSV Files/Word_Association_Trends.csv')

# Find the rising queries based on Keyword
print('Finding Rising Queries')
risingQueries(userText)

# Find the top queries based on Keyword
print('Finding Top Queries')
topQueries(userText)

# Find the rising topics based on Keyword
print('Finding Rising Topics')
risingTopics(userText)

# Find the rising topics based on Keyword
print('Finding Top Topics')
topTopics(userText)

# Append all to the same list with the original Keyword
suggestions = suggestions + risingQueriesVAR + topQueriesVAR
print('All Suggestions are: ', suggestions)

# Find the best locations based on user input
print('Finding City Data')
cityData(userText)

print('Finding Metro Data')
metroData(userText)

print('Finding Region Data')
regionData(userText)

# Find Current Trends
print('Finding Current Trends')
currentTrends()

# Find the rising Youtube queries based on Keyword
print('Finding the rising Youtube queries based on %s' % userText)
yt_risingQueries(userText)

# Find the top Youtube queries based on Keyword
print('Finding the Top Youtube queries based on %s' % userText)
yt_topQueries(userText)

# Find the rising Youtube topics based on Keyword
print('Finding Youtube Data on %s' % userText)
youtube_api(userText)

# print('Finding Twitter Hashtag Data')
#twitter_data(userText)

# Upload everything to google sheets
fileManager()

for item in FILE_LIST:
    print('Uploading %s to DataBase' % (item))
    sheetsUpload(item, item)
    time.sleep(10)

print('Report Created')

