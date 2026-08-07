class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subsets):
            res.append(subsets[:])

            for j in range(i ,len(nums)):
                subsets.append(nums[j])
                dfs(j + 1, subsets)
                subsets.pop()

        dfs(0, [])
        return res