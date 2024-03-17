from src.design_twitter import Twitter


def test_design_twitter():
    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.postTweet(1, 3)
    twitter.getNewsFeed(1) == [3, 5]


def test_design_twitter_v2():
    twitter = Twitter()
    twitter.postTweet(1, 5)
    twitter.postTweet(1, 3)
    twitter.getNewsFeed(1) == [3, 5]
