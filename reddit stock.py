# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:08:14 2021

@author: user
"""

import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import praw
import csv

reddit = praw.Reddit(client_id='C8shbaiLBqm1nQ',
                client_secret='lV0s0XZHvPpPsQhZPQtJKXznCwv2pA',
                user_agent='Scraping Example')

# get 10 hot posts from the MachineLearning subreddit

posts = []
ml_subreddit = reddit.subreddit('wallstreetbets')
for post in ml_subreddit.hot(limit=1000):
    posts.append([post.title, post.score, post.upvote_ratio, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score','upvote_ratio', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])


#print(posts[posts['title'].str.contains('TR')])

# insert stocks list
with open('tickers.csv','r') as csv_file:
    lines = csv_file.readlines()

stocks= []

for line in lines:
    data = line.rstrip('\n')
    stocks.append(data)

#with open("tickers.csv", "r") as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')

for s in stocks:
    count = posts[posts['title'].str.contains(s)]
    if len(count) > 5 and len(s) > 1 :
        print(s, len(count))

tickers = ['AR','EC', 'RE','ES','HE','LL','OR','RS','RS','SB','SE','ST']
for t in tickers:
    print(posts[posts['title'].str.contains(str(t))])



