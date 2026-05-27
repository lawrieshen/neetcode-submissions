class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counter = Counter(nums)

        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        while heap:
            _, num = heap.pop()
            result.append(num)

        return result