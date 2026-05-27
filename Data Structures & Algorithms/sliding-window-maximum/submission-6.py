class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maintain a dq to always keeps track to the max value (similar to max heap)
        if not nums:
            return []

        heap = []
        result = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                result.append(-heap[0][0]) 
        
        return result