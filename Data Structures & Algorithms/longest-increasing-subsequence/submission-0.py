class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []

        # find the left most postion to insert
        def binary_search(dp, target):
            left, right = 0, len(dp) - 1
            while left <= right:
                mid = (left + right) // 2
                if dp[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

        for num in nums:
            pos = binary_search(dp, num)

            if pos == len(dp):
                dp.append(num)
            else:
                dp[pos] = num

        return len(dp)