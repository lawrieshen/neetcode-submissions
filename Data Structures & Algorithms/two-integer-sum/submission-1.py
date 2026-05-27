class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        
        cache = {} # {num: index}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in cache:
                return [cache[complement], index]
            else:
                cache[num] = index
        
        return []