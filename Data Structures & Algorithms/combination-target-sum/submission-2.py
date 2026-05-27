class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(start, path):
            if sum(path) > target:
                return

            if sum(path) == target:
                res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i, path)
                path.pop()

        backtracking(0, [])
        return res