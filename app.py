!pip install snscrape
!pip install vaderSentiment

import pandas as pd
import numpy as np
import csv
import snscrape.modules.twitter as sntwitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datetime as dt
import time

# Generating datetime objects
from datetime import datetime, timedelta
now = datetime.now()
now = now.strftime('%Y-%m-%d')
yesterday = datetime.now() - timedelta(days = 1)
yesterday = yesterday.strftime('%Y-%m-%d')
print(yesterday)

keyword = input('Enter a topic or keyword, please:')

maxTweets = 80000


#Open/create a file to append data to
csvFile = open(keyword +'-sentiment-' + now + '.csv', 'a', newline='', encoding='utf8')

#Use csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['id','date','tweet',])


for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' lang:id since:' +  '2020-03-15' + ' until:' + now + ' -filter:links -filter:replies').get_items()):
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.id, tweet.date, tweet.content])
csvFile.close()
