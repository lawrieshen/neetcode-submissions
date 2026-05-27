class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, path, total):
            if total == target:
                res.append(path[:])
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                path.append(nums[j])
                backtrack(j, path, total + nums[j])
                path.pop()

        backtrack(0, [], 0)
        return res