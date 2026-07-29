class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache = {}

        for i, num in enumerate(numbers):
            complement = target - num
            if complement in cache:
                return [cache[complement] + 1, i + 1]
            cache[num] = i

        return []