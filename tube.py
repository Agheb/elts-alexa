#!/usr/bin/env
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config import youtube_api

DEVELOPER_KEY = youtube_api['key']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube():

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)


def channelList():

    # response of type dict

    return youtube().playlistItems().list(part='snippet', playlistId='UUsK8wjQhmpPSgRJ55mgxQkw').execute()


def channelStat():

    return youtube().channels().list(part='statistics', id=' UCsK8wjQhmpPSgRJ55mgxQkw').execute()


def getLatestVid():

    list_response = channelList()['items'][0]['snippet']
    results = {}
    results['title'] = list_response['title']
    results['publishedAt'] = list_response['publishedAt']
    results['videoId'] = list_response['resourceId']['videoId']

    return results


def currentFollower():

    stat_response = channelStat()['items'][0]['statistics']['subscriberCount']
    stat_result = {}
    stat_result['subscriberCount'] = stat_response

    return stat_result['subscriberCount']


if __name__ == '__main__':

    try:
        print getLatestVid()['title']
    except HttpError, e:
        print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)
