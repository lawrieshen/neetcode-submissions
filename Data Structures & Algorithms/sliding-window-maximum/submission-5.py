class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maintain a dq to always keeps track to the max value (similar to max heap)
        if not nums:
            return []

        dq = deque()
        result = []

        for i in range(len(nums)):
            # keeps the window size to k
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # only keeps the pop out the smaller value
            while dq and nums[dq[-1]] <  nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result