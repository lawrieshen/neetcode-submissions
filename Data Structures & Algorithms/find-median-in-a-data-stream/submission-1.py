class MedianFinder:

    def __init__(self):
        self.small = []  # max-heap via negatives
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # make sure every value in small <= every value in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # rebalance sizes so large has either same number or 1 extra
        if len(self.small) > len(self.large):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        return (self.large[0] - self.small[0]) / 2