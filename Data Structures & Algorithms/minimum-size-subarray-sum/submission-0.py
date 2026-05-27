class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minWindow = float('inf')
        summ = 0

        for right in range(len(nums)):
            summ += nums[right]

            while summ >= target:
                minWindow = min(minWindow, right - left + 1)
                summ -= nums[left]
                left += 1

        return 0 if minWindow == float('inf') else minWindow