class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return []

        cache = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in cache:
                return [cache[complement], i]
            else:
                cache[num] = i

        return []