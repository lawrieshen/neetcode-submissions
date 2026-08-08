class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])

            for i in range(start, len(nums)):
                if total + nums[i] > target:
                    return
                path.append(nums[i])
                backtrack(i, path, total + nums[i])
                path.pop()

        backtrack(0, [], 0)
        return res

        # Time: O(2^(t/m))
        # Space: O(t/m) 
        # where t us the given target and m is min(nums)