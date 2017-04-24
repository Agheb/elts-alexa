# ELTS Alexa Skill 

This skill is for the amazing people behind 
[eyeslovetosee](www.eyeslovetosee.de).
It has been developed using the [Alexa Skills Kit](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit) in Python.

The current version is for internal use only; other features may be added in the future.

### Current features:

* Read latest articles of [eyeslovetosee](www.eyeslovetosee.de)
* Get relevant key-metrics of eyeslovetosee's youtube channel (i.e follower count, latest video etc)
* Display useful 'cards' in Alexa App

### Dependencies 
* [Flask-Ask](https://github.com/johnwheeler/flask-ask) - Flask Extension for building Alex Skills 
* [Feedparser](http://pythonhosted.org/feedparser/)-  Python module for downloading and parsing RSS feeds
* [Youtube Data API](https://developers.google.com/youtube/v3/)

### Deployment (using AWS Lambda) 
[Zappa](https://github.com/Miserlou/Zappa)

