#!/usr/bin/env python
import feedparser
import logging
import sys
import time
from config import rss_feed
from operator import itemgetter

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

RSS_PATH = rss_feed['general']


def parse_RSS_Feed(rss_path):
    logging.info('%s ---> parsing RSS Feed' %(str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))))
    return feedparser.parse(rss_path)


def getPosts(numberOfEntries=5):
    '''
    default set to last 5 posts
    TODO: article should not exceed 8000 characters
    '''
    content = parse_RSS_Feed(RSS_PATH)
    posts = []
    for eachEntry in content.entries[0:numberOfEntries]:
        entry = {}
        entry['title'] = eachEntry.title
        entry['link'] = eachEntry.link
        entry['description'] = eachEntry.description
        entry['pubDate'] = eachEntry.published
        posts.append(entry)

    return posts



if __name__ == '__main__':
    # e = parse_RSS_Feed(RSS_PATH)
    print getPosts()
