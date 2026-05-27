class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # n belongs to [1 ... len(nums) + 1]
        # use input as memory

        # turn existing negative num or out of range  in nums into zero
        for i, num in enumerate(nums):
            if num < 0 or num > len(nums):
                nums[i] = 0
        # loop thru nums check if num belongs to [1 ... len(nums)]
        for num in nums:
            if num == 0:
                continue
            
            if 1 <= abs(num) <= len(nums):
                index = abs(num) - 1
                if nums[index] > 0:
                    nums[index] = nums[index] * -1
                elif nums[index] == 0:
                    nums[index] = -1
            
        # checking negativity to find the smallest missing positive
        for i, num in enumerate(nums):
            if num >= 0:
                return i + 1

        return len(nums) + 1