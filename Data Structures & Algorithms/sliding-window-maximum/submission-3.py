class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        n = len(nums)
        
        dq = deque() # storing the indices
        result = []

        for i in range(n):
            
            # shrinking value that's outside of the left boundary
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)

            # Start adding results once the first full window is formed
            if i >= k - 1:
                result.append(nums[dq[0]])  # Max of current window
                
        return result