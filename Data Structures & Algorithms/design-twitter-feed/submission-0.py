class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.followers_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds = []
        following = self.followers_map[userId] | {userId}
        for followee in following:
            tweets = self.tweets[followee]
            for tweet in tweets:
                heapq.heappush(feeds, tweet)
                if len(feeds) > 10:
                    heapq.heappop(feeds)
        
        return [heapq.heappop(feeds)[1] for _ in range(len(feeds))][::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers_map[followerId].discard(followeeId)
