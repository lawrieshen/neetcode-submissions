class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtracking(start, path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    backtracking(i + 1, path)
                    path.pop()
                    used[i] = False

        backtracking(0, [])
        return res