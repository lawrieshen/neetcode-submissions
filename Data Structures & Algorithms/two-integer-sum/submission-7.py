class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in cache:
                return [cache[complement], i]
            
            if num not in cache:
                cache[num] = i

        return []