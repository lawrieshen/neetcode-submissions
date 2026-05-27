class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = set()

        def backtrack(path):
            # base case
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.add(nums[i])
                backtrack(path)
                path.pop()
                used.discard(nums[i])

        backtrack([])
        return result