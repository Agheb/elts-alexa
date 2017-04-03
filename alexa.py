# -*- coding: utf-8 -*-
import logging
import dateutil.parser
import datetime
import pytz
from feed import postGrabber
from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

from tube import getLatestVid, currentFollower

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def new_ask():
    welcome = render_template('welcome')
    reprompt = render_template('reprompt')
    return question(welcome).reprompt(reprompt)


@ask.intent('LatestVidIntent')
def launchLatestVid():
    latest = getLatestVid()
    vtitle = latest["title"]
    # parse from ISO8601 to datetime
    vdate = getTimeDiff(latest["publishedAt"])
    # TODO Diff actual Time - publishedAt
    latest_msg = render_template('latest_video', date=vdate, title=vtitle)
    return statement(latest_msg)


@ask.intent('ReadPostsIntent')
def readPosts():
    # TODO modify getPost function to pass an argument
    posts = postGrabber()
    p_title = posts[3]['title']
    p_text = posts[3]['description']
    p_author = 'Marcus Schweighoefer'
    post_msg = render_template('readPost', title=p_title, text=p_text).encode('utf-8')
    return question(post_msg)


@ask.intent('AMAZON.NextIntent')
def nextPost():
    return readPosts()


@ask.intent('SubsCountYoutube')
def getSubscriberCount():
    subsCount = str(currentFollower())
    subsCount_msg = render_template('subsCountYoutube', count=subsCount)
    return statement(subsCount_msg)


@ask.intent('AMAZON.StopIntent')
def quit():
    return statement('Vielen Dank')


@ask.session_ended
def session_ended():
    return "", 200


def getTimeDiff(date):
    # TODO function is horseshit
    # parse ISO8601 str to datetime
    vdate = dateutil.parser.parse(date)
    # add timezone to become aware datetime object
    now = datetime.datetime.now(tz=pytz.utc)
    diff = now - vdate
    if diff.days < 0:
        return str(divmod(diff.total_seconds, 3600)) + ' ' + 'Stunden'
    else:
        return str(diff.days) + ' ' + 'Tagen'


if __name__ == '__main__':
    app.run(debug=True)
