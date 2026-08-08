class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            if total > target:
                return

            if total == target:
                res.append(path[:])

            for i in range(start, len(nums)):
                total += nums[i]
                path.append(nums[i])
                backtrack(i, path, total)
                total -= nums[i]
                path.pop()

        backtrack(0, [], 0)
        return res