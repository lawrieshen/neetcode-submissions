class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        cache = {}

        for i, number in enumerate(numbers):
            complement = target - number

            if complement in cache:
                return [cache[complement] + 1, i + 1]

            cache[number] = i

        return []