class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweet_map = defaultdict(list) # userId -> [[timestamp, tweetId]]
        self.following_map = defaultdict(set) # userId -> [followerId...]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.timestamp, tweetId])
        if len(self.tweet_map[userId]) > 10:
            self.tweet_map[userId].pop(0)
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        followees = self.following_map[userId] | {userId}

        for followee in followees:
            tweets = self.tweet_map[followee]
            for tweet in tweets:
                heapq.heappush(res, tweet)
                if len(res) > 10:
                    heapq.heappop(res)

        return [tid for _, tid in sorted(res, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)