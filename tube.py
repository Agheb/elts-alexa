#!/usr/bin/env
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from config import youtube_api

DEVELOPER_KEY = youtube_api['key']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube():

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)


def channelList():

    # https://www.googleapis.com/youtube/v3/playlistItems\?part\=snippet\&playlistId\=UUsK8wjQhmpPSgRJ55mgxQkw\&key\=\AIzaSyCNGralw9PmUPtnKiryYmKhliR9lkIAzQ4

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
        print getLatestVid()['publishedAt']
    except HttpError, e:
        print 'An HTTP error %d occurred:\n%s' % (e.resp.status, e.content)
