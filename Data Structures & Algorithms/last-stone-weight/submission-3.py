class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)

            new_stone = stone1 - stone2

            if new_stone >= 0:
                heapq.heappush(max_heap, -new_stone)

        return -max_heap[0]