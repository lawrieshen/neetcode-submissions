class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # order matters, contains duplicate
        res = []
        used = [False] * len(nums)
        nums.sort()


        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i, num in enumerate(nums):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(num)
                backtrack(path)
                used[i] = False
                path.pop()

        backtrack([])
        return res                