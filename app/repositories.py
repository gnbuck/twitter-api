# pylint: disable=missing-docstring

from .models import Tweet

class TweetRepository:
    def __init__(self):
        self.clear()

    def add(self, tweet):
        self.tweets.append(tweet)
        tweet.id = self.next_id
        self.next_id += 1

    def get(self, _id):
        for tweet in self.tweets:
            if tweet.id == _id:
                return tweet
        return None

    def clear(self):
        # tweet = Tweet("footest")
        # tweet.id = 0
        self.tweets = []
        self.next_id = 1
