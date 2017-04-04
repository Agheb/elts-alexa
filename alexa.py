# -*- coding: utf-8 -*-
import logging
import dateutil.parser
import datetime
import pytz
from feed import get_FeedItem
from flask import Flask, render_template

from flask_ask import Ask, statement, question, session
from tube import getLatestVid, currentFollower

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


def set_post_idx():
    post_idx = 0
    session.attributes['post_idx'] = post_idx
    return post_idx

@ask.launch
def new_ask():
    welcome = render_template('welcome')
    reprompt = render_template('reprompt')
    return question(welcome).reprompt(reprompt)


@ask.intent('ReadPostsIntent')
def readPost(post_idx):
    logging.info('%s Type',post_idx)

    if post_idx is None:
        post_idx = set_post_idx()

    tmp = get_FeedItem(post_idx)

    if tmp['shouldEndsession'] is True:
        return statement('Keine weitere Artikel verfügbar')

    else:
        # TODO: add real author to template
        txt = render_template('readPost',title=tmp['title'],text=tmp['description']).encode('utf-8')
        return question(txt)


@ask.intent('LatestVidIntent')
def launchLatestVid():
    latest = getLatestVid()
    vtitle = latest["title"]
    # parse from ISO8601 to datetime
    vdate = getTimeDiff(latest["publishedAt"])
    # TODO Diff actual Time - publishedAt
    latest_msg = render_template('latest_video', date=vdate, title=vtitle)
    return statement(latest_msg)


@ask.intent('SubsCountYoutube')
def getSubscriberCount():
    subsCount = str(currentFollower())
    subsCount_msg = render_template('subsCountYoutube', count=subsCount)
    return statement(subsCount_msg)


@ask.intent('AMAZON.StopIntent')
def quit():
    return statement('Bis zum naechsten Mal. Eyes love to see')


@ask.intent('AMAZON.NextIntent')
def nextPost():
    new_post_idx = session.attributes['post_idx'] + 1
    session.attributes['post_idx'] = new_post_idx

    return readPost(new_post_idx)

@ask.session_ended
def session_ended():
    logging.info("session ended")
    return "", 200


def getTimeDiff(date):
    # TODO function is horseshit
    # parse ISO8601 str to datetime
    vdate = dateutil.parser.parse(date)
    # add timezone to become aware datetime object
    now = datetime.datetime.now(tz=pytz.utc)
    diff = now - vdate
    if diff.days <= 0:
        return str(divmod(diff.total_seconds, 3600)) + ' ' + 'Stunden'
    else:
        return str(diff.days) + ' ' + 'Tagen'


if __name__ == '__main__':
    app.run(debug=True)
