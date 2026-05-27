class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        
        n = len(numbers)

        look_up = {}

        for i, num in enumerate(numbers):
            diff = target - num

            if diff in look_up:
                return [look_up[diff] + 1, i + 1]

            look_up[num] = i

        return []

