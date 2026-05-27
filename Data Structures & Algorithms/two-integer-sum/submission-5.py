class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []

        cache = {}

        for i, num in enumerate(nums):
            residual = target - num

            if residual in cache:
                return [cache[residual], i]

            cache[num] = i

        return []