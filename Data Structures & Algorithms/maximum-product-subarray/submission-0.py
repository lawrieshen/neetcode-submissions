class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        current_max = 1
        current_min = 1 # this will highly ;iekly to be negative as long as ther 's at least one negative element

        for num in nums:
            # (1) if num is positive (2) is num is negative (3) is num itself is max
            cache = current_max * num
            current_max = max(current_max * num, current_min * num, num)
            current_min = min(cache, current_min * num, num)

            res = max(res, current_max)

        return res
            