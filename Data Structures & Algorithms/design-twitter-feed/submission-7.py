class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []

        # include self
        self.followMap[userId].add(userId)

        # push latest tweet from each followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap and self.tweetMap[followeeId]:
                idx = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(max_heap, (-count, tweetId, followeeId, idx - 1))

        # get 10 most recent tweets
        while max_heap and len(res) < 10:
            negCount, tweetId, followeeId, idx = heapq.heappop(max_heap)
            res.append(tweetId)

            if idx >= 0:
                count, nextTweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(max_heap, (-count, nextTweetId, followeeId, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)