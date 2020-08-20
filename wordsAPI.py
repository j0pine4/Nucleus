import requests
import json
import pprint
import pandas as pd

wordsList = []

def wordsAPI(input):
    keyword = input
    apiKey = '3f35f80b-7846-4f5b-bba0-a8ba7e8ac47d'
    r = requests.get('https://api.wordassociations.net/associations/v1.0/json/search?apikey=3f35f80b-7846-4f5b-bba0-a8ba7e8ac47d&text=%s&lang=en&limit=25 HTTP/1.1' % keyword)
    data = r.json()

    item = data['response'][0]['items']

    for i in item:
        wordsList.append(i['item'])

    if len(wordsList) < 1:
        print('this list is empty')

        r = requests.get('https://api.wordassociations.net/associations/v1.0/json/search?apikey=3f35f80b-7846-4f5b-bba0-a8ba7e8ac47d&text=%s&lang=en&limit=25 HTTP/1.1' % 'null')
        data = r.json()

        item = data['response'][0]['items']

        for i in item:
            wordsList.append(i['item'])

        df = pd.DataFrame(wordsList)
        df.to_csv('wordAssociation.csv')

    else:
        df = pd.DataFrame(wordsList)
        df.to_csv('CSV Files/wordAssociation.csv')


























