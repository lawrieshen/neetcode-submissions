class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: clean up invalid values
        for i, num in enumerate(nums):
            if num < 1 or num > n:
                nums[i] = 0

        # Step 2: mark presence
        for num in nums:
            if num == 0:
                continue

            idx = abs(num) - 1
            if nums[idx] >= 0:
                nums[idx] = -nums[idx] if nums[idx] != 0 else -1

        # Step 3: find first missing
        for i, num in enumerate(nums):
            if num >= 0:
                return i + 1

        return n + 1
