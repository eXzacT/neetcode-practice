import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.counter = 0  # Used to fake time

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.tweets[user_id].append((self.counter, tweet_id))
        self.counter -= 1

    def getNewsFeed(self, user_id: int) -> list[int]:
        heap = [(timestamp, tweet_id) for timestamp, tweet_id in self.tweets[user_id]]+[(timestamp, tweet_id)
                                                                                        for followee_id in self.follows[user_id] for timestamp, tweet_id in self.tweets[followee_id]]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(min(10, len(heap)))]

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.follows[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.follows[follower_id].discard(followee_id)
