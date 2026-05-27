from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # at each index, what's the longest subsequence I can end here?

        # if we end at i, among all j < i where nums[j] < nums[i], what's LIS we canfind?
        
        # dp[i] represents the length of the longest increasing subsequence ending at i

        # to compute dp[i], look at every j < i.
        # If nums[j] < nums[i], then nums[i] can extend the LIS ending at j.
        # So dp[i] = max(dp[i], 1 + dp[j])

        # If no previous smaller element exists, dp[i] stays 1

        # dp = [1] * len(nums)

        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[i], 1 + dp[j])

        # return max(dp)

        tails = []

        for num in nums:
            i = bisect_left(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num
        return len(tails)

