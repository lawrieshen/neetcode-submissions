class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(i, j):
            if i == len(nums):
                return 0

            LIS = dfs(i + 1, j)

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))

            return LIS

        return dfs(0, -1)