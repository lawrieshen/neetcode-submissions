class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        current_sum = 0

        for num in nums:
            if current_sum < 0:
                current_sum = 0 # we start a new subarray
            current_sum += num
            res = max(res, current_sum)

        return res 
