class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]
        if n == 2: 
            return max(nums[0], nums[1])

        def rob_linear(arr):
            prev2 = 0
            prev1 = 0
            for val in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + val)
            return prev1

        # case A: skip first → rob nums[1:]
        # case B: skip last  → rob nums[:-1]
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))