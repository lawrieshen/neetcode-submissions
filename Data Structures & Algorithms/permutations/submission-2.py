class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(start, path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtracking(i + 1, path)
                    path.pop()

        backtracking(0, [])
        return res