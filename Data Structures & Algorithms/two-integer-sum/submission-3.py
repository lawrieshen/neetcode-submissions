class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        cache = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in cache:
                return [cache[complement], index]

            cache[num] = index

        return []