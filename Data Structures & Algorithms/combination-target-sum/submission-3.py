class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, path, total):
            if total > target:
                return

            if total == target:
                res.append(path[:])
                return

            for j in range(i, len(nums)):
                path.append(nums[j])
                backtrack(j, path, total + nums[j])
                path.pop()

        backtrack(0, [], 0)
        return res